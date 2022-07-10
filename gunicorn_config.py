#Web Server Production Configuration File
import multiprocessing

#Network Interfaces
bind = '0.0.0.0'
umask = 0o007

#Resource Configurations
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 10

#Preloading (Makes app use less memory)
preload_app = True
reload = True

#Logging
accesslog = '-'
errorlog = '-'
loglevel = 'debug'

