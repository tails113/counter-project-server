class Counter():

    def __init__( self, redis_database ):
        self.__database = redis_database
        self.__create()

    def __create( self ):
        check = self.__database.get('counter')
        if not check:
            self.__database.getset('ascending', 'true')
            self.__database.getset('counter', 0)
        
    def check_ascending( self ):
        if self.__database.get('ascending') == 'true':
            return True
        else:
            return False
        
    def get( self ):
        return self.__database.get('counter')

    def decrease( self ):
        self.__database.decr('counter', amount=1)
        if int(self.get()) <= 0:
            self.__database.getset('ascending', 'true')
        
    def increase( self ):
        self.__database.incr('counter', amount=1)
        if int(self.get()) >= 10:
            self.__database.getset('ascending', 'false')
