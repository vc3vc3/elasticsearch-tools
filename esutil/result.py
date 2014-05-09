from elasticsearch import RequestError

def acknowledge_result(self, result):
    """
    Interpret a result from an ElasticSearch API call and display it.
        result          Dictionary object from ElasticSearch API

    Returns
        error_status    Boolean value indicating if result was an error or not.
    """

    error_status = True

    if result and result.get('acknowledged'):
        print "acknowledged: %s" % result['acknowledged']
        error_status = False
    elif result.get('error'):
        print "error: %s" % result['error']
    else:
        raise RequestError("An unknown error occurred in your request.")

    return error_status