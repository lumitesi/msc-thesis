class NameServer(Thread):

	def __init__(self, config):
		# Thread configs
        Thread.__init__(self, name="Thread-NameServer")
        self.ns_ip = config["ip"]
        self.ns_port = config["port"]
        self.ns_db = config["dbFile"]

        # Pyro name server
        self.nameserver_uri, 
        self.nameserver_daemon, 
        self.broadcast_server = Pyro4.naming.startNS(host=self.ns_ip,
                                                     port=self.ns_port,
                                                     storage=self.ns_db)

        self.nameserver_daemon.combine(self.broadcast_server)


	def run(self):
        # This is triggered in the thread.start() call
        try:
            self.nameserver_daemon.requestLoop()
        finally:
            # clean up
            self.broadcast_server.close()
            self.nameserver_daemon.close()