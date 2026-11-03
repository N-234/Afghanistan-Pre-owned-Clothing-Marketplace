# Test Results – Sprint 3

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Tested By:** Both Developers (Frontend and Backend)  
**Sprint:** Sprint 3  
**Environment:** Local Development Environment (Flask and SQLite)

---

## Test Summary

| Metric | Value |
|--------|-------|
| Total Test Cases | 8 |
| Passed | 8 |
| Failed | 0 |
| Pass Rate | 100% |
| Critical Bugs | 0 |
| Major Bugs | 0 |
| Minor Bugs | 0 |

---

## Test Execution Details

### TC-001: Access Seller Dashboard
**Status:** ✅ PASSED

**Summary:** Logged-in users were able to open their dashboard and view their own clothing listings.

---

### TC-002: View Active Listings
**Status:** ✅ PASSED

**Summary:** The dashboard displayed the seller's available listings correctly.

---

### TC-003: View Sold Listings
**Status:** ✅ PASSED

**Summary:** Listings marked as sold appeared in the sold section of the dashboard.

---

### TC-004: Edit an Existing Listing
**Status:** ✅ PASSED

**Summary:** Sellers were able to open their own listings, update the information, and save the changes successfully.

---

### TC-005: Prevent Editing Another User's Listing
**Status:** ✅ PASSED

**Summary:** The system checked listing ownership and prevented users from editing listings that belonged to other sellers.

---

### TC-006: Mark a Listing as Sold
**Status:** ✅ PASSED

**Summary:** Sellers were able to change an available listing's status to sold, and the updated status appeared in the dashboard.

---

### TC-007: Mark a Listing as Unavailable
**Status:** ✅ PASSED

**Summary:** Sellers were able to mark their available listings as unavailable.

---

### TC-008: Remove a Listing
**Status:** ✅ PASSED

**Summary:** Sellers were able to remove their listings from the marketplace. The listing status changed to removed instead of permanently deleting the database record.

---

## Bugs Found

No major or minor bugs were recorded during Sprint 3 testing.

---

## Security and Validation Testing

The following checks were included:

- Only logged-in users could access their seller dashboard.
- Sellers could edit only their own listings.
- Listing ownership was checked before changing status.
- Listing status changes were handled by the backend.
- Removed listings were not permanently deleted from the database.

---

## Recommendations for Sprint 4

- Add a messaging system between buyers and sellers.
- Add an inbox to display received messages.
- Add a reporting option for inappropriate listings.
- Add notifications for new messages.
- Continue testing user permissions and interactions.

---

## Test Coverage

- **Functional Testing:** Seller dashboard, editing, and listing status changes.
- **Database Testing:** Updating and retrieving listing information.
- **Security Testing:** Login sessions and listing ownership.
- **Status Testing:** Available, sold, unavailable, and removed listings.
- **UI Testing:** Dashboard and edit listing pages.

---

## Conclusion

Sprint 3 testing focused on helping sellers manage their clothing listings. Users could access their dashboards, edit their own listings, and change listing statuses. The tested features worked as expected, and no major issues were recorded.

**Overall Quality:** Good  
**Ready for Sprint Review:** Yes
