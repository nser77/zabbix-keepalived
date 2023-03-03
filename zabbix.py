class ZabbixInterface:
    @staticmethod
    def output(data):
        if not type(data) == str:
            raise Exception("Unsupported ZABBIX data type")

        print(data)
        return

    @staticmethod
    def intToString(intput):
        if not type(intput) == int:
            raise Exception("intToString accepts only <int> type as input")

        return str(intput)

    @staticmethod
    def boolToInt(boolput):
        if not type(boolput) == bool:
            raise Exception("boolToInt accepts only <bool> type as input")

        if boolput:
            return int(1)
        else:
            return int(0)
