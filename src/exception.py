import sys

def error_message_detail(error_message, error_details: sys):
    _,_,exc_tb = error_details.exc_info()

    filename = exc_tb.tb_frame.f_code.co_filename
    linenum = exc_tb.tb_lineno
    msg = str(error_message)

    error_report = (
        f"Error occured in file - {filename}\n"
        f"Error occured in linenum - {linenum}\n"
        f"Error message - {msg}"
    )

    return error_report


class CustomException(Exception):
    def __init__(self,error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        return self.error_message