#!/usr/bin/env sh
rm db.sqlite3
./manage.py syncdb --noinput --verbosity=1
./manage.py migrate --noinput --verbosity=1
./manage.py loaddata \
    auth_admin \
    site_test \
    repertory_test \
    member_test \
    events_test \
    recording_test
