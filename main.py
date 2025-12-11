from dotenv import load_dotenv
from logging_config import get_logger, set_rpa_workflow_name, set_rpa_module_name, set_rpa_argo_workflow_name, set_rpa_workflow_run_guid
import os
import sys
# Load environment variables
load_dotenv()

# Get a logger for this script
logger = get_logger(__name__)
set_rpa_module_name("Argo Worflow") # This is set once for the whole module, not per script
set_rpa_workflow_name(os.getenv("RPA_NAME","RPA_NAME_WF")) # This should be set from the argo workflow with environment variable
set_rpa_argo_workflow_name(os.getenv("ARGO_WORKFLOW_NAME","ARGO_WORKFLOW_WF")) # This should be set from the argo workflow with environment variable
set_rpa_workflow_run_guid(os.getenv("RPA_RUN_GUID","RPA_RUN_GUID_WF")) # This should be set from the argo workflow with environment variable


def main():
    message = sys.argv[1]  # first argument
    logger.info(f"Received message: {message}")
    # logger.info(f"Step: {args.step if args.step else 'N/A'} | Message: {args.message} | Completed")

if __name__ == "__main__":
    logger.info("Executing Python script.")
    main()
    logger.info("Python script successfully executed.")