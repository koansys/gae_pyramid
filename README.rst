============================================
 README: Pyramid on Google App Engine (GAE)
============================================

The buildouts and instructions we've seen seem to be lagging Pyramid's
development. @Sontek (John Anderson) pointed us at work he worked on
that Reed cloned to https://gist.github.com/reedobrien/10663097

Install
=======

Virtualenv::
  virtualenv .venv
  source .venv/bin/activate

Buildout::

  python bootstrap.py
  bin/buildout -v

This creates a python and GAE tools in the bin/ directory including:

* appcfg: for deploying to GAE cloud
* dev_appserver: for deploying to local GAE emulator

