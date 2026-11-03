# Test Results – Sprint 2

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Tested By:** Both Developers (Frontend and Backend)  
**Sprint:** Sprint 2  
**Environment:** Local Development Environment (Flask and SQLite)

---

## Test Summary

| Metric | Value |
|--------|-------|
| Total Test Cases | 9 |
| Passed | 9 |
| Failed | 0 |
| Pass Rate | 100% |
| Critical Bugs | 0 |
| Major Bugs | 0 |
| Minor Bugs | 0 |

---

## Test Execution Details

### TC-001: Search Clothing by Name
**Status:** ✅ PASSED

**Summary:** Users were able to search for clothing by entering a keyword. The system displayed listings that matched the search.

---

### TC-002: Filter Listings by Size
**Status:** ✅ PASSED

**Summary:** Users were able to select a size and view only the clothing listings that matched the selected size.

---

### TC-003: Filter Listings by Maximum Price
**Status:** ✅ PASSED

**Summary:** The price filter worked correctly and displayed listings within the selected maximum price.

---

### TC-004: Filter Listings by Category
**Status:** ✅ PASSED

**Summary:** Users were able to select a clothing category and view matching listings.

---

### TC-005: Filter Listings by Condition
**Status:** ✅ PASSED

**Summary:** Users were able to filter clothing based on its condition.

---

### TC-006: Clear Search and Filters
**Status:** ✅ PASSED

**Summary:** The clear filters option removed the selected search and filter values and displayed the listings again.

---

### TC-007: Upload a Valid Clothing Photo
**Status:** ✅ PASSED

**Summary:** Users were able to upload supported image formats, and the photo was saved and displayed with the clothing listing.

---

### TC-008: Validate Clothing Listing Information
**Status:** ✅ PASSED

**Summary:** The system checked the listing information before saving it and prevented invalid or missing required information from being submitted.

---

### TC-009: Validate Uploaded Photo
**Status:** ✅ PASSED

**Summary:** The system checked the uploaded photo format and file size. Unsupported formats and files larger than the allowed limit were rejected.

---

## Bugs Found

No major or minor bugs were recorded during Sprint 2 testing.

---

## Security and Validation Testing

The following checks were included:

- Required listing information was validated.
- Invalid price values were checked.
- Only supported image formats were accepted.
- Image uploads were limited to the allowed file size.
- Search and filter inputs were handled by the backend.

---

## Recommendations for Sprint 3

- Add a seller dashboard to manage personal listings.
- Allow sellers to edit their clothing listings.
- Add options to mark listings as sold or unavailable.
- Improve the process of managing existing listings.
- Continue testing listing ownership and permissions.

---

## Test Coverage

- **Functional Testing:** Search, filtering, and photo uploads.
- **Database Testing:** Saving and retrieving listing information.
- **Validation Testing:** Listing information and uploaded photos.
- **UI Testing:** Search bar, filters, and listing display.

---

## Conclusion

Sprint 2 testing focused on helping users find clothing more easily and allowing sellers to upload clothing listings with their information and photos. The tested features worked as expected, and no major issues were recorded.

**Overall Quality:** Good  
**Ready for Sprint Review:** Yes
