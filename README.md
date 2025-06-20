# detection_configuration_auditd

Данная работа создана для того, чтобы реализовать упрощенную работу с auditd

```
sudo detection_configuration_auditd/auditd.sh
```


```
alyona@alyona:~/repo/detection_configuration_auditd$ sudo '/home/alyona/repo/detection_configuration_auditd/auditd.sh' 
--- Установка зависимостей ---
Requirement already satisfied: PyYAML in /usr/lib/python3/dist-packages (from -r /home/alyona/repo/detection_configuration_auditd/requirements.txt (line 1)) (5.4.1)
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
--- Создание правил ---
Установлено правило: auditctl -w /home/alyona/tetetetet.txt -p rwxa
--- Список созданных правил ---
-w /home/alyona/tetetetet.txt -p rwxa
```

чтобы видеть последние записи

```
alyona@alyona:~/repo/detection_configuration_auditd$ sudo tail -f /var/log/audit/audit.log
type=SERVICE_START msg=audit(1750417206.249:10805): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=unconfined msg='unit=st_client_gui comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'UID="root" AUID="unset"
type=SERVICE_STOP msg=audit(1750417206.253:10806): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=unconfined msg='unit=st_client_gui comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=failed'UID="root" AUID="unset"
type=SERVICE_START msg=audit(1750417211.501:10807): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=unconfined msg='unit=st_client_gui comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'UID="root" AUID="unset"
type=SERVICE_STOP msg=audit(1750417211.501:10808): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=unconfined msg='unit=st_client_gui comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'UID="root" AUID="unset"
type=SERVICE_START msg=audit(1750417211.513:10809): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=unconfined msg='unit=st_client_gui comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'UID="root" AUID="unset"
type=SERVICE_STOP msg=audit(1750417211.517:10810): pid=1 uid=0 auid=4294967295 ses=4294967295 subj=unconfined msg='unit=st_client_gui comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=failed'UID="root" AUID="unset"
type=USER_ACCT msg=audit(1750417212.065:10811): pid=141880 uid=1000 auid=4294967295 ses=4294967295 subj=unconfined msg='op=PAM:accounting grantors=pam_permit acct="alyona" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/1 res=success'UID="alyona" AUID="unset"
type=USER_CMD msg=audit(1750417212.065:10812): pid=141880 uid=1000 auid=4294967295 ses=4294967295 subj=unconfined msg='cwd="/home/alyona/repo/detection_configuration_auditd" cmd=7461696C202D66202F7661722F6C6F672F61756469742F61756469742E6C6F67 exe="/usr/bin/sudo" terminal=pts/1 res=success'UID="alyona" AUID="unset"
type=CRED_REFR msg=audit(1750417212.065:10813): pid=141880 uid=1000 auid=4294967295 ses=4294967295 subj=unconfined msg='op=PAM:setcred grantors=pam_permit,pam_cap acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/1 res=success'UID="alyona" AUID="unset"
type=USER_START msg=audit(1750417212.065:10814): pid=141880 uid=1000 auid=4294967295 ses=4294967295 subj=unconfined msg='op=PAM:session_open grantors=pam_limits,pam_env,pam_env,pam_permit,pam_umask,pam_unix acct="root" exe="/usr/bin/sudo" hostname=? addr=? terminal=/dev/pts/1 res=success'UID="alyona" AUID="unset"
```

ausearch для поиска конкретных событий в логах аудита

```
alyona@alyona:~/repo/detection_configuration_auditd$ sudo ausearch -f /home/alyona/tetetetet.txt
----
time->Fri Jun 20 13:55:01 2025
type=PROCTITLE msg=audit(1750416901.317:10504): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750416901.317:10504): item=0 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750416901.317:10504): cwd="/home/alyona"
type=SYSCALL msg=audit(1750416901.317:10504): arch=c000003e syscall=257 success=yes exit=12 a0=ffffff9c a1=55dae8525370 a2=0 a3=0 items=1 ppid=1 pid=141323 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
----
time->Fri Jun 20 13:55:13 2025
type=PROCTITLE msg=audit(1750416913.717:10517): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750416913.717:10517): item=0 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750416913.717:10517): cwd="/home/alyona"
type=SYSCALL msg=audit(1750416913.717:10517): arch=c000003e syscall=257 success=yes exit=14 a0=ffffff9c a1=559e4f58f460 a2=0 a3=0 items=1 ppid=1 pid=141538 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
----
time->Fri Jun 20 13:55:18 2025
type=PROCTITLE msg=audit(1750416918.033:10522): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750416918.033:10522): item=1 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750416918.033:10522): item=0 name="/home/alyona/" inode=655362 dev=08:03 mode=040750 ouid=1000 ogid=1000 rdev=00:00 nametype=PARENT cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750416918.033:10522): cwd="/home/alyona"
type=SYSCALL msg=audit(1750416918.033:10522): arch=c000003e syscall=257 success=no exit=-17 a0=ffffff9c a1=559e4f58f460 a2=800c1 a3=1b6 items=2 ppid=1 pid=141538 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
----
time->Fri Jun 20 13:55:18 2025
type=PROCTITLE msg=audit(1750416918.033:10523): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750416918.033:10523): item=1 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750416918.033:10523): item=0 name="/home/alyona/" inode=655362 dev=08:03 mode=040750 ouid=1000 ogid=1000 rdev=00:00 nametype=PARENT cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750416918.033:10523): cwd="/home/alyona"
type=SYSCALL msg=audit(1750416918.033:10523): arch=c000003e syscall=257 success=yes exit=11 a0=ffffff9c a1=559e4f58f460 a2=20041 a3=1b6 items=2 ppid=1 pid=141538 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
----
time->Fri Jun 20 13:55:18 2025
type=PROCTITLE msg=audit(1750416918.113:10524): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750416918.113:10524): item=4 name="/home/alyona/tetetetet.txt" inode=655993 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=CREATE cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750416918.113:10524): item=3 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=DELETE cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750416918.113:10524): item=2 name="/home/alyona/.goutputstream-Q9CG82" inode=655993 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=DELETE cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750416918.113:10524): item=1 name="/home/alyona/" inode=655362 dev=08:03 mode=040750 ouid=1000 ogid=1000 rdev=00:00 nametype=PARENT cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750416918.113:10524): item=0 name="/home/alyona/" inode=655362 dev=08:03 mode=040750 ouid=1000 ogid=1000 rdev=00:00 nametype=PARENT cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750416918.113:10524): cwd="/home/alyona"
type=SYSCALL msg=audit(1750416918.113:10524): arch=c000003e syscall=82 success=yes exit=0 a0=559e50332910 a1=559e50438110 a2=0 a3=0 items=5 ppid=1 pid=141538 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
----
time->Fri Jun 20 13:59:45 2025
type=PROCTITLE msg=audit(1750417185.101:10783): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750417185.101:10783): item=0 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750417185.101:10783): cwd="/home/alyona"
type=SYSCALL msg=audit(1750417185.101:10783): arch=c000003e syscall=257 success=yes exit=12 a0=ffffff9c a1=55cc0ffe2500 a2=0 a3=0 items=1 ppid=1 pid=141844 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
----
time->Fri Jun 20 13:59:48 2025
type=PROCTITLE msg=audit(1750417188.685:10788): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750417188.685:10788): item=1 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750417188.685:10788): item=0 name="/home/alyona/" inode=655362 dev=08:03 mode=040750 ouid=1000 ogid=1000 rdev=00:00 nametype=PARENT cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750417188.685:10788): cwd="/home/alyona"
type=SYSCALL msg=audit(1750417188.685:10788): arch=c000003e syscall=257 success=no exit=-17 a0=ffffff9c a1=55cc0ffe2500 a2=800c1 a3=1b6 items=2 ppid=1 pid=141844 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
----
time->Fri Jun 20 13:59:48 2025
type=PROCTITLE msg=audit(1750417188.685:10789): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750417188.685:10789): item=1 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750417188.685:10789): item=0 name="/home/alyona/" inode=655362 dev=08:03 mode=040750 ouid=1000 ogid=1000 rdev=00:00 nametype=PARENT cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750417188.685:10789): cwd="/home/alyona"
type=SYSCALL msg=audit(1750417188.685:10789): arch=c000003e syscall=257 success=yes exit=11 a0=ffffff9c a1=55cc0ffe2500 a2=20041 a3=1b6 items=2 ppid=1 pid=141844 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
----
time->Fri Jun 20 13:59:48 2025
type=PROCTITLE msg=audit(1750417188.705:10790): proctitle=6D6F757365706164002F686F6D652F616C796F6E612F7465746574657465742E747874
type=PATH msg=audit(1750417188.705:10790): item=4 name="/home/alyona/tetetetet.txt" inode=655993 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=CREATE cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750417188.705:10790): item=3 name="/home/alyona/tetetetet.txt" inode=655675 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=DELETE cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750417188.705:10790): item=2 name="/home/alyona/.goutputstream-KQIU82" inode=655993 dev=08:03 mode=0100644 ouid=1000 ogid=1000 rdev=00:00 nametype=DELETE cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750417188.705:10790): item=1 name="/home/alyona/" inode=655362 dev=08:03 mode=040750 ouid=1000 ogid=1000 rdev=00:00 nametype=PARENT cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=PATH msg=audit(1750417188.705:10790): item=0 name="/home/alyona/" inode=655362 dev=08:03 mode=040750 ouid=1000 ogid=1000 rdev=00:00 nametype=PARENT cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0 cap_frootid=0
type=CWD msg=audit(1750417188.705:10790): cwd="/home/alyona"
type=SYSCALL msg=audit(1750417188.705:10790): arch=c000003e syscall=82 success=yes exit=0 a0=55cc10dc4480 a1=55cc10d51a30 a2=0 a3=0 items=5 ppid=1 pid=141844 auid=4294967295 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=4294967295 comm="mousepad" exe="/usr/bin/mousepad" subj=unconfined key=(null)
alyona@alyona:~/repo/detection_configuration_auditd$
```