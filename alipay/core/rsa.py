

class Sign(object):
    def __init__(self, s=None):
        self._s_ = s

    def SignRSA(self, waitSignString=None):
        # paramsStrings = []
        # for key, value in paramsDict.items():
        #     if value == None:
        #         continue
        #     # LOG.info('%s = %s', key, value)
        #     if type(value) == type({}):
        #         paramsStrings.append(u'%s=%s' % (key, json.dumps(value, cls=CJsonEncoder)))
        #     else:
        #         paramsStrings.append(u'%s=%s' % (key, unicode(value)))
        # paramsStrings.sort()
        # LOG.info(paramsStrings)
        # waitSignString = self._dictParamsToString_(paramsDict)
        if not waitSignString:
            waitSignString = self._s_
        LOG.info(waitSignString)
        priKey = rsa.PrivateKey.load_pkcs1(RSA_PRIVATE_KEY)
        msgEncrypted = rsa.sign(waitSignString, priKey, 'SHA-1')
        return base64.b64encode(msgEncrypted)


