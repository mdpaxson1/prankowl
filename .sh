git filter-branch --parent-filter '
    read parent
    if [ "$parent" = "-p ad3ce9f2ad6cdbc43788520dc58d0e8f5e3601d9" ]
    then
        echo
    else
        echo "$parent"
    fi'
