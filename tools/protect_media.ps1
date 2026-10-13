# Восстановление junction'ов (ZnT1 -> ZnT1_MEDIA).
# Реальные медиафайлы хранятся ВНЕ репозитория: D:\gameMake\ZnT-1\ZnT1_MEDIA\
# Если git clean или другой инструмент удалил junction — этот скрипт вернёт
# связь. Он только СОЗДАЁТ ссылки, никогда ничего не удаляет.
# Запуск: powershell -ExecutionPolicy Bypass -File tools\protect_media.ps1
$media = "D:\gameMake\ZnT-1\ZnT1_MEDIA"
# пара: куда -> какая целевая папка (относительно ZnT1_MEDIA)
$links = @(
    @{ link = "game\audio";   dir = "audio" },
    @{ link = "game\images";  dir = "images" },
    @{ link = "game\gui";     dir = "gui" },
    @{ link = "game\video";   dir = "video" },
    @{ link = "wav_files";    dir = "wav_files" }
)

foreach ($e in $links) {
    $link = $e.link
    $target = Join-Path $media $e.dir
    if (-not (Test-Path $target)) {
        Write-Output "ERROR: target missing: $target"
        continue
    }
    if (Test-Path $link) {
        $item = Get-Item $link -Force
        if ($item.LinkType -eq "Junction") {
            Write-Output "ok (junction): $link"
        } else {
            Write-Output "ERROR: $link exists as a REAL directory - target data may be at risk, inspect manually"
        }
    } else {
        New-Item -ItemType Junction -Path $link -Target $target | Out-Null
        Write-Output "restored junction: $link"
    }
}
