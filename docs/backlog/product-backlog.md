# Afghan Girls' Pre-Owned Clothes Marketplace Backlog

**Sara Qateh (Product Owner)**  
**Software Engineering**  
** October 5 2026**

---

## 1. Introduction

The Product Backlog is the main repository for all work required to develop the Afghan Girls' Pre-Owned Clothes Marketplace. It contains the functional and technical requirements of the system and is organized according to the needs of buyers, sellers, and administrators.

The backlog contains 20 User Stories. Each User Story includes acceptance criteria, priority, effort estimation, sprint assignment, and the responsible development team member.

The Product Backlog will be continuously reviewed and refined throughout the Scrum process. Items may be reprioritized when the team receives feedback from users or identifies new technical or functional requirements.

---

## 2. Functional Backlog Items (User Stories)

| ID | User Story | Acceptance Criteria | Priority | Estimation | Sprint | Responsible |
| --- | --- | --- | --- | --- | --- | --- |
| US-001 | As a girl visiting the website, I want to create an account so that I can buy or sell pre-owned clothes. | Registration requires valid information; account is created successfully; duplicate email is rejected. | High | 5 | Sprint 1 | Developer 1 |
| US-002 | As a registered user, I want to log in securely so that I can access my personal account. | Correct credentials allow access; incorrect credentials are rejected; user can log out successfully. | High | 3 | Sprint 1 | Developer 1 |
| US-003 | As a buyer, I want to see recently added clothes so that I can discover new items. | Recently added products are displayed in the correct order with basic product information. | High | 5 | Sprint 1 | Developer 2 |
| US-004 | As a buyer, I want to view clothes by category so that I can focus on the type of clothing I need. | Categories such as dresses, shirts, trousers, jackets, and traditional clothes are available. | High | 5 | Sprint 1 | Developer 2 |
| US-005 | As a buyer, I want to search for a clothing item by its name or keyword so that I do not have to browse every listing. | Search returns matching products; appropriate message appears when no results are found. | High | 5 | Sprint 2 | Developer 2 |
| US-006 | As a buyer, I want to filter clothes by size and price so that I can find products within my needs and budget. | Size and price filters work correctly and display matching results. | High | 5 | Sprint 2 | Developer 2 + Developer 1 |
| US-007 | As a buyer, I want to see the condition of a clothing item so that I know whether it is suitable before contacting the seller. | Seller must select a condition such as new, like new, good, or used; condition is displayed on the product page. | High | 3 | Sprint 2 | Developer 1 |
| US-008 | As a seller, I want to upload photos of my clothes so that buyers can see the actual item before contacting me. | Seller can upload valid image files; images are displayed with the listing. | High | 5 | Sprint 2 | Developer 2 |
| US-009 | As a seller, I want to provide the price, size, condition, and description of my clothes so that buyers have enough information about the item. | Required product information must be completed before the listing can be published. | High | 5 | Sprint 2 | Developer 1 + Developer 2 |
| US-010 | As a seller, I want to see all of my posted clothes in one place so that I can easily manage my listings. | Seller dashboard displays active, sold, and removed listings belonging to that seller. | Medium | 5 | Sprint 3 | Developer 2 |
| US-011 | As a seller, I want to update the information of my clothing listing so that I can correct or change details. | Seller can edit their own listing; changes are saved and displayed correctly. | Medium | 3 | Sprint 3 | Developer 1 |
| US-012 | As a seller, I want to mark a clothing item as sold so that other buyers know that it is no longer available. | Seller can mark the item as sold; product status changes from available to sold. | Medium | 3 | Sprint 3 | Developer 1 |
| US-013 | As a buyer, I want to save clothes that I like so that I can return to them later. | Buyer can add and remove products from saved items; saved items remain in their account. | Medium | 5 | Sprint 3 | Developer 2 |
| US-014 | As a buyer, I want to contact a seller about a specific clothing item so that I can ask questions before making a decision. | Buyer can send a message associated with the selected listing; seller can receive and view it. | High | 8 | Sprint 3 | Developer 1 + Developer 2 |
| US-015 | As a user, I want to report a suspicious or inappropriate listing so that the administrator can review it. | User can submit a report with a reason; report is stored for administrator review. | Medium | 5 | Sprint 4 | Developer 2 + Developer 1 |
| US-016 | As an administrator, I want to review reported listings so that I can remove inappropriate content from the marketplace. | Admin can view reports, inspect listings, and remove content when necessary. | High | 5 | Sprint 4 | Developer 1 |
| US-017 | As an administrator, I want to manage registered users so that I can prevent misuse of the platform. | Admin can view user accounts and deactivate accounts that violate platform rules. | High | 5 | Sprint 4 | Developer 1 |
| US-018 | As an administrator, I want to see the status of clothing listings so that I can monitor the marketplace. | Admin can view available, sold, and removed listings. | Medium | 3 | Sprint 4 | Developer 2 |
| US-019 | As a user, I want to receive notifications when important activity occurs on my account so that I do not miss updates. | Notifications are generated for relevant events such as new messages or listing changes. | Medium | 5 | Sprint 5 | Developer 2 |
| US-020 | As a user, I want the website to work properly on my phone and computer so that I can use the marketplace from different devices. | Main pages and functions work correctly on mobile, tablet, and desktop screens. | High | 8 | Sprint 5 | Developer 2 + Developer 1 |

---

## 3. Enhancement Tasks

| ID | Enhancement | Acceptance Criteria | Priority | Estimation | Sprint | Responsible |
| --- | --- | --- | --- | --- | --- | --- |
| ENHANCE-001 | Improve product image loading and display. | Images are clear, properly sized, and load efficiently. | Medium | 3 | Sprint 5 | Developer 1 |
| ENHANCE-002 | Add sorting options for clothing listings. | Users can sort products by price, newest listings, and other available options. | Medium | 5 | Sprint 5 | Developer 2 |
| ENHANCE-003 | Improve the mobile user interface. | Navigation and product pages are easy to use on smaller screens. | Medium | 3 | Sprint 5 | Developer 2 |

---

## 4. Non-Functional Backlog Items

| ID | Technical Story | Acceptance Criteria | Priority | Estimation | Sprint | Responsible |
| --- | --- | --- | --- | --- | --- | --- |
| NFR-001 | As a system, I should protect user passwords so that account information remains secure. | Passwords are not stored as plain text and protected pages require authentication. | High | 5 | Sprint 1 | Developer 1 |
| NFR-002 | As a system, I should respond quickly to normal user requests so that users can browse the marketplace comfortably. | Main pages respond within an acceptable time under normal system load. | High | 5 | Sprint 2 | Developer 2 |
| NFR-003 | As a system, I should prevent invalid information from being submitted. | Forms validate required fields, formats, prices, and uploaded files. | High | 5 | Sprint 2 | Developer 1 |
| NFR-004 | As a system, I should restrict administrative functions to authorized administrators. | Normal users cannot access administrator pages or functions. | High | 5 | Sprint 4 | Developer 1 |
| NFR-005 | As a system, I should maintain user and product data reliably. | Data is stored correctly and can be retrieved without unexpected loss. | High | 5 | Sprint 3 | Developer 1 |
| NFR-006 | As a system, I should work on commonly used browsers. | Website is tested on Chrome, Edge, and Firefox. | Medium | 3 | Sprint 5 | Developer 2 |
| NFR-007 | As a system, I should have a maintainable code structure so that future developers can update the system. | Code is organized, documented, and reviewed. | Medium | 5 | Sprint 5 | Developer 1 + Developer 2 |
| NFR-008 | As a system, I should provide a simple interface so that users with basic computer skills can navigate the website. | Main functions are clearly labeled and users can navigate between major pages easily. | High | 5 | Sprint 1 | Developer 2 |

---

## 5. Prioritization Strategy

### High Priority

High-priority items represent the core functionality needed for the marketplace to operate. These include:

- Account registration and login
- Browsing clothes
- Viewing clothing categories
- Searching and filtering
- Viewing product condition
- Uploading clothing images
- Adding product information
- Contacting sellers
- Reporting inappropriate listings
- Administrator management
- Security and access control

### Medium Priority

Medium-priority items improve the overall experience and management of the platform. These include:

- Managing personal listings
- Editing listings
- Marking products as sold
- Saving favorite clothes
- User management
- Listing monitoring
- Notifications
- Data reliability

### Low Priority

Optional improvements that are not required for the basic marketplace include additional sorting options, advanced image optimization, and other interface enhancements.

---

## 6. Guidance on Sprint Planning

### Sprint 1: User Access and Product Discovery

**Main Goal:** Build the foundation of the marketplace and allow users to access and explore the system.

**Main Work:**

- US-001: Create Account
- US-002: Login and Logout
- US-003: Recently Added Clothes
- US-004: Clothing Categories
- NFR-001: Password Security
- NFR-008: Simple User Interface

**Expected Increment:**  
Users can create accounts, log in, browse recently added clothes, and explore different clothing categories.

---

### Sprint 2: Product Search and Seller Listings

**Main Goal:** Allow buyers to find suitable clothes and sellers to create detailed listings.

**Main Work:**

- US-005: Search
- US-006: Size and Price Filters
- US-007: Clothing Condition
- US-008: Upload Product Photos
- US-009: Product Information
- NFR-002: Performance
- NFR-003: Input Validation

**Expected Increment:**  
Buyers can search and filter clothes, while sellers can create complete clothing listings with photos and product information.

---

### Sprint 3: Listing Management and Communication

**Main Goal:** Give sellers control over their listings and allow buyers to communicate with sellers.

**Main Work:**

- US-010: View My Listings
- US-011: Edit Listing
- US-012: Mark as Sold
- US-013: Save Clothes
- US-014: Contact Seller
- NFR-005: Data Reliability

**Expected Increment:**  
Sellers can manage their listings, buyers can save products and contact sellers, and products can be marked as sold.

---

### Sprint 4: Administration and Safety

**Main Goal:** Provide administrators with the tools needed to maintain a safe marketplace.

**Main Work:**

- US-015: Report Listing
- US-016: Review Reports
- US-017: Manage Users
- US-018: Monitor Listings
- NFR-004: Administrator Access

**Expected Increment:**  
Users can report inappropriate content, while administrators can review reports and manage users and listings.

---

### Sprint 5: Notifications and Final Improvements

**Main Goal:** Improve the overall quality, accessibility, and usability of the marketplace.

**Main Work:**

- US-019: Notifications
- US-020: Mobile and Desktop Support
- Enhancement Tasks
- Browser Testing
- Final Testing
- Bug Fixing
- Documentation

**Expected Increment:**  
A complete, responsive, tested marketplace ready for final demonstration.

---

## 7. Product Backlog Refinement

The Product Backlog will be reviewed throughout the project. Requirements may change based on feedback from users, the Product Owner, developers, and Scrum team members.

For example, if users report that searching by size and price is more important than saving clothes, the Product Owner may move the filtering feature to a higher priority and postpone the saved-items feature.

Similarly, if the team discovers a security issue, the related technical story may be moved to an earlier sprint.

This allows the team to follow the Scrum principle of continuously adapting the product according to changing requirements and user needs.

---

## 8. Definition of Done

A User Story will be considered Done when:

- The feature has been developed.
- All acceptance criteria have been satisfied.
- The feature has been tested.
- Major bugs have been fixed.
- The code has been reviewed.
- The feature has been integrated into the current system.
- Required documentation has been updated.
- The work has been committed to GitHub.
- The Product Owner has reviewed and accepted the completed work.

---

**Prepared by:** Sara Qateh (Product Owner)  
**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Date:** October 5, 2026
