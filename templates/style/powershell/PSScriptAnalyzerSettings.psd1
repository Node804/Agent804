@{
    # Optional baseline, not an exhaustive security ruleset.
    IncludeRules = @(
        'PSUseConsistentIndentation'
        'PSUseConsistentWhitespace'
        'PSPlaceOpenBrace'
        'PSPlaceCloseBrace'
        'PSUseCorrectCasing'
        'PSUseApprovedVerbs'
        'PSAvoidUsingInvokeExpression'
        'PSAvoidUsingPlainTextForPassword'
    )
    Rules = @{
        PSUseConsistentIndentation = @{
            Enable = $true
            Kind = 'space'
            IndentationSize = 4
        }
        PSUseConsistentWhitespace = @{ Enable = $true }
        PSPlaceOpenBrace = @{ Enable = $true; OnSameLine = $true }
        PSPlaceCloseBrace = @{ Enable = $true; NoEmptyLineBefore = $true }
        PSUseCorrectCasing = @{ Enable = $true }
    }
}
