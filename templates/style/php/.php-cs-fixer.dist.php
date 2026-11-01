<?php

declare(strict_types=1);

// Optional PER 3.0 recommendation. Copy to the project root and review Finder scope.
$finder = PhpCsFixer\Finder::create()
    ->in(__DIR__)
    ->exclude('vendor');

return (new PhpCsFixer\Config())
    ->setRiskyAllowed(false)
    ->setRules(['@PER-CS3x0' => true])
    ->setFinder($finder);
