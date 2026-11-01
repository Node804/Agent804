[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string[]]$Path,
    [switch]$Fix
)

$ErrorActionPreference = 'Stop'
Import-Module PSScriptAnalyzer -ErrorAction Stop
$settings = Join-Path $PSScriptRoot 'PSScriptAnalyzerSettings.psd1'
$failed = $false
foreach ($item in $Path) {
    $file = (Resolve-Path -LiteralPath $item -ErrorAction Stop).Path
    if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
        throw "Supply explicit maintained file paths, not directories: $file"
    }
    $source = [System.IO.File]::ReadAllText($file)
    $formatted = Invoke-Formatter -ScriptDefinition $source -Settings $settings
    $formatted = ($formatted -replace "`r`n?", "`n").TrimEnd("`n") + "`n"
    if ($Fix) {
        [System.IO.File]::WriteAllText($file, $formatted, [System.Text.UTF8Encoding]::new($false))
    } elseif ($source -cne $formatted) {
        Write-Output "Formatting required: $file"
        $failed = $true
    }
    $diagnostics = @(Invoke-ScriptAnalyzer -Path $file -Settings $settings)
    if ($diagnostics.Count -gt 0) {
        $diagnostics | Format-Table -AutoSize | Out-Host
        $failed = $true
    }
}
if ($failed) {
    exit 1
}
