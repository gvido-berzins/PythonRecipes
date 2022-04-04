"""
Summary:
    Duplicate an existing spreadsheet to a folder with sharing
Description:
    Script creates a new spreadsheet based on a template and copies to
    to the specified folder (using it's Google Drive folder ID) and gives
    write permissions to a given domain.
"""

#!/usr/bin/env python3.10
import gspread
from gspread import Client, Spreadsheet


def copy_spreadsheet(
    gc: Client, template_id: str, title: str, folder_id: str, copy_permissions: bool
) -> Spreadsheet:
    return gc.copy(
        template_id, title=title, folder_id=folder_id, copy_permissions=copy_permissions
    )


def share_spreadsheet(
    sh: Spreadsheet, account_type: str, perm_type: str, role: str, with_link: bool
) -> Spreadsheet:
    """Share the spreadsheet to a user"""
    return sh.share(account_type, perm_type=perm_type, role=role, with_link=with_link)


def duplicate_spreadsheet(
    gc: Client, template_id: str, sheet_title: str, folder_id: str
) -> Spreadsheet:
    """Duplicate the template spreadsheet into a specific folder"""
    new_sh = copy_spreadsheet(
        gc, template_id, title=sheet_title, folder_id=folder_id, copy_permissions=True
    )
    share_spreadsheet(
        new_sh, "example.com", perm_type="domain", role="writer", with_link=False
    )
    return new_sh


if __name__ == "__main__":
    template_title = "TEMPLATE"
    drive_folder_id = "SomeDriveID"
    new_sheet_title = "Fresh"
    google_client: Client = gspread.service_account(
        filename="/path/to/service_account.json"
    )
    template_id = google_client.open(template_title).id

    new_sheet = duplicate_spreadsheet(
        gc=google_client,
        template_id=template_id,
        sheet_title=new_sheet_title,
        folder_id=drive_folder_id,
    )
