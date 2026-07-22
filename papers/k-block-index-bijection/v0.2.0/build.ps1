[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$paperRoot = $PSScriptRoot
$latexRoot = Join-Path $PSScriptRoot 'latex'
$buildRoot = Join-Path $latexRoot 'build'
$outputPdf = Join-Path $paperRoot 'pdf\k-block-index-bijection-v0.2.0-open-review.pdf'

$latexmk = Get-Command latexmk -ErrorAction SilentlyContinue
if ($null -eq $latexmk) {
    throw 'latexmk was not found on PATH. Install TeX Live or expose latexmk before building.'
}

Push-Location $latexRoot
try {
    & $latexmk.Source -pdf -bibtex -interaction=nonstopmode -halt-on-error "-outdir=$buildRoot" main.tex
    if ($LASTEXITCODE -ne 0) {
        throw "latexmk failed with exit code $LASTEXITCODE."
    }
    Copy-Item -LiteralPath (Join-Path $buildRoot 'main.pdf') -Destination $outputPdf -Force
}
finally {
    Pop-Location
}
