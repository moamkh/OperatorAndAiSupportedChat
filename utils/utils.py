class ResponseUtils:
    def error_context(status:bool=True,msg:str=None) -> dict:
        if not msg:
            raise ValueError("no msg suplied.")
        context = {
            'status':status,
            'message':msg
        }
        return context

    def ok_context(status:bool=True,msg:str='',data=None) -> dict:
        if not data:
            raise ValueError("no data suplied.")
        context = {
            'status':status,
            'message':msg,
            'data':data
        }
        return context
    
    @classmethod
    def error_serializer(cls,serializer_errors:dict):
        for error in serializer_errors.keys():
            if error == 'non_field_errors':
                error_msg = f'{serializer_errors[error][0]}'
            else:
                error_msg = f'Field {error} : {serializer_errors[error][0]}'
            break
        return cls.error_context(status=False,msg =error_msg)