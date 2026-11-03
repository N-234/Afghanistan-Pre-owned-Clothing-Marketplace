# Test Results – Sprint 4

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Tested By:** Both Developers (Frontend and Backend)  
**Sprint:** Sprint 4  
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

### TC-001: Contact Seller
**Status:** ✅ PASSED

**Summary:** Logged-in users were able to open the contact seller form from a clothing listing and send a message to the seller.

---

### TC-002: Prevent Contacting Own Listing
**Status:** ✅ PASSED

**Summary:** The system prevented users from sending messages to themselves through their own listings.

---

### TC-003: Message Validation
**Status:** ✅ PASSED

**Summary:** The system checked the message before saving it and prevented empty messages from being submitted.

---

### TC-004: View Received Messages in Inbox
**Status:** ✅ PASSED

**Summary:** Users were able to open their inbox and view messages received from other users, including the related listing information.

---

### TC-005: New Message Notifications
**Status:** ✅ PASSED

**Summary:** A notification was created when a seller received a new message. The notification bell displayed the unread notification count.

---

### TC-006: Mark Notifications as Read
**Status:** ✅ PASSED

**Summary:** Opening the inbox marked new message notifications as read, and the unread notification count was updated.

---

### TC-007: Report a Clothing Listing
**Status:** ✅ PASSED

**Summary:** Users were able to submit a report for a clothing listing by selecting a reason and submitting the report.

---

### TC-008: Save a Clothing Listing
**Status:** ✅ PASSED

**Summary:** Users were able to save clothing listings for later access.

---

### TC-009: Unsave a Clothing Listing
**Status:** ✅ PASSED

**Summary:** Users were able to remove previously saved listings from their saved items.

---

## Bugs Found

No major or minor bugs were recorded during Sprint 4 testing.

---

## Security and Validation Testing

The following checks were included:

- Only logged-in users could access protected messaging features.
- Users could not contact themselves through their own listings.
- Empty messages were rejected.
- Messages were stored with the correct sender, receiver, and listing information.
- Notifications were associated with the correct user.
- Users could only access their own messages and saved items.

---

## Recommendations for Sprint 5

- Complete the admin dashboard features.
- Improve report management and review.
- Add user account management for administrators.
- Add listing management options for administrators.
- Test admin permissions and access restrictions.

---

## Test Coverage

- **Functional Testing:** Contact seller, inbox, notifications, reporting, and saved listings.
- **Database Testing:** Messages, notifications, reports, and saved items.
- **Security Testing:** User sessions and access permissions.
- **Validation Testing:** Message and report submissions.
- **UI Testing:** Contact seller form, inbox, and notification bell.

---

## Conclusion

Sprint 4 testing focused on communication between buyers and sellers and additional marketplace features. The tested functions allowed users to send and receive messages, view notifications, report listings, and save clothing items.

**Overall Quality:** Good  
**Ready for Sprint Review:** Yes
