# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import VCF libraries
from lib import databases as dblib

# Import Standard Python libraries
import os
import sys

# Hesiod Header and Log init
liblog.hesiod_print_header()

# Local functions
def help_stdout():
    print("HELP MENU: hesiod-db.py [options]")
    print("Enter options 1x per run, do not add all parameters at once!")
    print("--help option to see this menu.")
    print("")
    print("--cassandra option to deploy a Cassandra database.")
    print("")
    print("--hadoop option to deploy a Hadoop database.")
    print("")
    print("--maria option to deploy a Maria database.")
    print("")
    print("--mongo option to deploy a Mongo database.")
    print("")
    print("--mysql option to deploy a MySQL database.")
    print("")
    print("--postgres option to deploy a Postgres database.")
    print("")
    print("--redis option to deploy a Redis database.")
    print("")
    print("")

def match_help(args):
    if '--help' in args:
        return True

def match_cassandra(args):
    if '--cassandra' in args:
        return True

def match_hadoop(args):
    if '--hadoop' in args:
        return True

def match_maria(args):
    if '--maria' in args:
        return True

def match_mongo(args):
    if '--mongo' in args:
        return True

def match_mysql(args):
    if '--mysql' in args:
        return True
                    
def match_postgres(args):
    if '--postgres' in args:
        return True

def match_redis(args):
    if '--redis' in args:
        return True

# Match args
match_found = False 
match_found = match_help(sys.argv)
if match_found :
    help_stdout()
    sys.exit() 

else:
    match_found = False 
    match_found = match_cassandra(sys.argv)
    if match_found :
        dblib.deploy_cassandra()
        sys.exit() 

    match_found = False 
    match_found = match_hadoop(sys.argv)
    if match_found :
        dblib.deploy_hadoop()
        sys.exit() 

    match_found = False 
    match_found = match_maria(sys.argv)
    if match_found :
        dblib.deploy_maria()
        sys.exit() 

    match_found = False 
    match_found = match_mongo(sys.argv)
    if match_found :
        dblib.deploy_mongo()
        sys.exit() 

    match_found = False 
    match_found = match_mysql(sys.argv)
    if match_found :
        dblib.deploy_mysql()
        sys.exit() 

    match_found = False 
    match_found = match_postgres(sys.argv)
    if match_found :
        dblib.deploy_postgres()
        sys.exit() 

    match_found = False 
    match_found = match_redis(sys.argv)
    if match_found :
        dblib.deploy_redis()
        sys.exit()        

    else:
        #Default
        print("No parameters found. Defaulting to --help menu.")
        print("")
        help_stdout()
        sys.exit()

