# Test Results – Sprint 1

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Tested By:** Both Developers (Frontend and Backend)  
**Sprint:** Sprint 1  
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

### TC-001: User Registration with Valid Information
**Status:** ✅ PASSED

**Summary:** The user was able to register with valid information. The account was successfully created and stored in the database.

---

### TC-002: User Registration with an Existing Email
**Status:** ✅ PASSED

**Summary:** The system checked whether the email was already registered and prevented the creation of another account with the same email.

---

### TC-003: User Login with Correct Credentials
**Status:** ✅ PASSED

**Summary:** Login worked correctly with valid email and password. The user was logged in and redirected to the homepage.

---

### TC-004: User Login with Incorrect Credentials
**Status:** ✅ PASSED

**Summary:** The system rejected incorrect login information and displayed an appropriate error message.

---

### TC-005: User Logout
**Status:** ✅ PASSED

**Summary:** The logout function worked correctly. The user's session was cleared, and the user was logged out.

---

### TC-006: Display Recently Added Clothes
**Status:** ✅ PASSED

**Summary:** The homepage displayed clothing listings retrieved from the database, with recently added listings appearing first.

---

### TC-007: Browse Clothing Categories
**Status:** ✅ PASSED

**Summary:** Users were able to browse clothing categories and view the related listings.

---

### TC-008: Password Security
**Status:** ✅ PASSED

**Summary:** User passwords were stored as hashed values in the database instead of being saved as plain text.

---

## Bugs Found

No major or minor bugs were recorded during Sprint 1 testing.

---

## Security Testing

The following basic security checks were tested:

- Passwords were hashed before being stored.
- Duplicate email registration was prevented.
- Incorrect login credentials were rejected.
- User sessions were cleared after logout.

---

## Recommendations for Sprint 2

- Add search functionality for clothing listings.
- Add filters for size, price, and condition.
- Improve clothing listing information.
- Add image upload and validation.
- Continue testing user input validation.

---

## Test Coverage

- **Functional Testing:** Account registration, login, logout, and browsing.
- **Database Testing:** User accounts and clothing listings.
- **Security Testing:** Password hashing and basic session handling.
- **UI Testing:** Registration, login, and homepage display.

---

## Conclusion

Sprint 1 testing focused on the main features of the marketplace, including user registration, login, logout, and browsing clothing listings. The tested features worked as expected, and no major issues were recorded.

**Overall Quality:** Good  
**Ready for Sprint Review:** Yes
