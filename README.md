Homepage of SMARTSTUDY
======================

a yet another *flat* site for a mobile app development company.

Demo site : <http://www.smartstudy.co.kr>


FEATURES
--------

  - Listing company crews.
  - Listing companys apps.
  - Resume management.


INSTALL
-------

    git clone git://github.com/lqez/smartstudy-home.git
    cd smartstudy-home
    mkvirtualenv smartstudy-home
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate --all --fake
    python manage.py runserver


That's all!
