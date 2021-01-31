import xmlrpc.client

url = 'https://demo.odoo.com/start'

class OdooApiConnect:

    def __init__(self, url):
        info = xmlrpc.client.ServerProxy(url).start()
        self.url, self.db, self.username, self.password = \
            info['host'], info['database'], info['user'], info['password']
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.login()
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))


    def login(self):
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})
    
    def search_model(self, model, params=[[]]):
        return self.models.execute_kw(self.db, self.uid, self.password, model, 'search' , params)


api = OdooApiConnect(url)
print(api.search_model('res.partner'))
