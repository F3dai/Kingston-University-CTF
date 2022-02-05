#!/bin/sh

ls -1 /tmp/initdb.d/*.sql | while read file; do
  mysql -uroot -ptoor < $file
done
