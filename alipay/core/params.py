# -*- coding:utf-8 -*-

class Params(object):
    def __init__(self, **kwargs):
        self._p_ = kwargs

    def ToString(self, ):
        return self._dictParamsToString_(self._p_)

    def _dictParamsToString_(self, paramsDict):
        paramsStrings = []
        for key, value in paramsDict.items():
            if value == None or len(value) == 0:
                continue
            # LOG.info('%s = %s', key, value)
            if type(value) == type({}):
                paramsStrings.append(u'%s=%s' % (key, json.dumps(value, cls=CJsonEncoder, sort_keys=True, separators=(',',':'))))
            else:
                paramsStrings.append(u'%s=%s' % (key, unicode(value)))
        paramsStrings.sort()
        # LOG.info(paramsStrings)
        s = u'&'.join(paramsStrings)
        # return urllib.quote(s.encode('utf-8'))
        return s.encode('utf-8')

    