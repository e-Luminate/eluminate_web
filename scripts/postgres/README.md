These scripts are needed when we backup with Point In Time Restore (PITR) method.
archive_wal 
is used to archive Postgre's WAL files to a save place

do_base_backup 
takes a snapshot of teh file system, though without WAL files being available teh backup is of little use.

The scripts should be installed typically in in ~postgres/scripts.


