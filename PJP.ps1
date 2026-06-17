$outputFile = ".\backend_all_code.txt"
if (Test-Path $outputFile) { Remove-Item $outputFile }

Get-ChildItem -Path ".\src\main\java" -Filter *.java -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $relative = $filePath.Replace((Get-Location).Path, '')
    
    # 寫入分隔線
    "// ========================================================" | Out-File -FilePath $outputFile -Append -Encoding default
    "// FILE: $relative" | Out-File -FilePath $outputFile -Append -Encoding default
    "// ========================================================" | Out-File -FilePath $outputFile -Append -Encoding default
    
    # 讀取並寫入 Java 內容
    Get-Content -Path $filePath -Encoding default | Out-File -FilePath $outputFile -Append -Encoding default
    
    # 換行
    "`n`n" | Out-File -FilePath $outputFile -Append -Encoding default
}

write-host "Success! Please check backend_all_code.txt" -ForegroundColor Green