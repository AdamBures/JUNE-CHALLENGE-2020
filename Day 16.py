class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            ip = IP.split('.')
            if len(ip) != 4:                            # length has to be 4
                return 'Neither'        
            for x in ip:    
                if len(x) == 0 or len(x) > 3:           # empty or more than allocated length
                    return 'Neither'
                if x[0] == '0' and len(x) > 1:          # leading 0
                    return 'Neither'
                for i in x:
                    if i not in '0123456789':           # check the domain
                        return 'Neither'
                if int(x) < 0 or int(x) > 255:          # check the domain
                    return 'Neither'
            return 'IPv4'
        else:
            ip = IP.split(':')
            if len(ip) != 8:                            # length to be 8
                return 'Neither'
            for x in ip:
                if len(x)  == 0:                        # 2 consecutive ::
                    return 'Neither'
                if len(x) > 4:                          # not a valid number
                    return 'Neither'
                for i in x:
                    if i not in '0123456789abcdefABCDEF':       # check for domain
                        return 'Neither'
            return 'IPv6'
