### service monitoring script

sname=$1
stitle=$2
server=$(/bin/hostname)

if ! systemctl is-active --quiet $sname; then
        slack "WARNING: On server $server, $stitle found stopped, restarting."
        # systemctl is-active --quiet $sname; echo $?
        sudo service $sname restart

        if systemctl is-active --quiet $sname; then
                slack "INFO: On server $server, $stitle restarted."
                #systemctl is-active --quiet $sname; echo $?
        else
                slack "WARNING: On server $server failed to restart $stitle."
        fi
fi

###
