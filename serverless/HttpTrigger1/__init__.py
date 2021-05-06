# This code to be implemented in Azure Functions for serverless cloud computing

import logging
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import azure.functions as func

# HTTP Trigger on Azure Functions
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Request Parsed')
    k=get_content()
    
    return func.HttpResponse(
        k,
        status_code=200,
        headers={'content-type':'text/html'},
    )

# defining a function that returns HTML code to fetch captured documents to a website

def get_content():

    #Azure tokens
    connect_str = '[REMOVED FOR PRIVACY]'
    sas_token ='[REMOVED FOR PRIVACY]'
    
    #Azure blob URL
    url ='https://storageaccountonline.blob.core.windows.net/'
    k = ''
 
    # Generate HTML code
    src = '<img src="'
    src_end = '" class="figure-img img-fluid rounded" alt="..." height="300" width="300">'
    js='<script>setTimeout(() => {location.reload(true);}, 10000)</script>\n'
    init1 = '<HTML>\n<HEAD>\n'
    init2='<TITLE>\n Braille Cam Captured Notes \n</TITLE>\n</HEAD>\n<BODY>\n<figure class="figure">\n'
    end = '\n<figcaption class="figure-caption text-center">These are the captured docuemnts</figcaption>\n</figure>\n</BODY>\n</HTML>'
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

	# Container name
        read_data = 'sample-data'
        url = url+read_data+'/'
        container_client = blob_service_client.get_container_client(read_data)

	# getting list of blobs
        blob_list = container_client.list_blobs()       
        namelist=[]
        
	# namelist[] stores blobs in first to last manner of blob creation
        for blob in blob_list:
            namelist.append(blob.name)

        # sort namelist in Descending order
        namelist=sorted(namelist, reverse=True)

	# referencing each blob
        for name in namelist:
            k = k+src+url+name+sas_token+src_end

    except Exception as ex:
        logging.info('Exception:')
        logging.info(ex)
    
    # Final HTML code
    k = init1+js+init2+k+end
    return k
