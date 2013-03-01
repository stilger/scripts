#!/usr/bin/env bash

#Set paths
export NN_TMUX="/path/to/newznab/tmux"
export BACKUP_PATH=$NN_TMUX"/backup"
cd $NN_TMUX
# create a backup directory first IE: mkdir backup

BackupDefaults()
{
echo "Backing up current defaults.sh"
if [ -d "$BACKUP_PATH" ]; then
cp -p $NN_TMUX/defaults.sh $BACKUP_PATH/defaults.sh.`date +"%Y.%m.%d-%H.%M.%S"`
echo "backup of current defaults.sh complete"
else
echo "Backup did not run. Backup Directory does not exist"
echo "Please create the backup directory"
echo "Exiting."
exit 0
fi
}

GitFetch()
{
echo "Running git fetch -V"
git fetch -v
echo "git fetch complete"
}

CreatePatch()
{
echo "Running git diff against master to create patch file"
git diff master origin/master config.sh > changes.patch
echo "git diff complete"
}

ApplyPatch()
{
echo "Applying patch to defaults.sh"
patch defaults.sh < changes.patch
echo "Patch applied"
echo "Fix any hunks that did not apply correctly."
echo "Now run git pull to update to current tmux version"
}

# Comment any that you do not want to run below. 
BackupDefaults
GitFetch
CreatePatch
ApplyPatch
