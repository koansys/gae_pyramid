============================================
 README: Pyramid on Google App Engine (GAE)
============================================

The buildouts and instructions we've seen seem to be lagging Pyramid's
development. @Sontek (John Anderson) pointed us at work he worked on
that we're starting for here.

Install
=======

We're using "git flow" so you probably want to check out the 'develop'
branch.

Virtualenv::

  virtualenv .venv
  source .venv/bin/activate

Buildout::

  ./.venv/bin/python bootstrap.py
  ./bin/buildout

The buildout takes a while because it downloads the GAE SDK; you might
want to set up a buildout download-cache.

This creates a python and GAE tools in the bin/ directory including:

* appcfg: for deploying to GAE cloud
* dev_appserver: for deploying to local GAE emulator

Run
===

Run the local developer app server against the application in the app/
directory. It looks for the app.yaml file there which tells it the
app's entry point and what GAE modules to use (e.g., PIL, webob).  If
there's a appengine_config.py, you call specify directories to add ot
the sys.path; this is where we specify pyramid and its dependencies,
which the builtout put into app/dist/::

  ./bin/dev_appserver app/

It'll tell you what ports it picks for the application, admin and API
server::

  INFO     2014-04-15 17:18:52,936 api_server.py:171] Starting API server at: http://localhost:60189
  INFO     2014-04-15 17:18:52,940 dispatcher.py:182] Starting module "default" running at: http://localhost:8080
  INFO     2014-04-15 17:18:52,948 admin_server.py:117] Starting admin server at: http://localhost:8000
  INFO     2014-04-15 17:18:56,181 module.py:627] default: "GET / HTTP/1.1" 200 21


Push to GAE
===========

Create a new application at https://appengine.google.com/

Create a new release branch::

  $ git flow release start 1.0

 update $BUILDOUT_DIR/app/app.yaml::

  application: <YOURAPPNAME_ID>
  version: <APPROPRIATEVERSION_IS_PROBABLY_1>

  $ ./bin/appcfg --oauth2 update app/

Then commit, tag and push::

  $ git flow release finish 1.0
  $ git push --tags
  $ git push --all
