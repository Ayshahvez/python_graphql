from .models import Tokens

def query_getall_transfer_tokens_resolver(obj, info):
    try:
        transfer_token = [transfer_token.to_dict() for transfer_token in Tokens.query.all()]
        print(transfer_token)
        payload = {
            "success": True,
            "transfer_token": transfer_token
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    print(payload)
    return payload

    from ariadne import convert_kwargs_to_snake_case

#@convert_kwargs_to_snake_case
def query_get_transfer_token_resolver(obj, info, id):
    try:
        #transfer_token = Tokens.query.limit(id).all()
        # [:5]   query.filter().limit(id).all()
        transfer_token = [transfer_token.to_dict() for transfer_token in Tokens.query.limit(id)]
        payload = {
            "success": True,
            "transfer_token": transfer_token
        }
        #print(payload)
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    
    return payload