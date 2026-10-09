# Software Requirements Specification

## Afghan Girls' Pre-Owned Clothes Marketplace

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace    
**Date:** October 5, 2026  
**Prepared by:** Project Team  

---

## 1. Introduction

### 1.1 Purpose

This document defines the functional and non-functional requirements of the Afghan Girls' Pre-Owned Clothes Marketplace.

The system is a web-based marketplace that allows users to create accounts, browse pre-owned clothes, create and manage clothing listings, search and filter products, and communicate with sellers.

This document focuses on what the system must provide. Detailed project background and objectives are maintained separately in the Project Overview, while User Stories, priorities, estimations, and Sprint assignments are maintained in the Product Backlog.

---

### 1.2 Scope

The system will provide an online marketplace for pre-owned clothes.

The main users of the system are:

- Buyers
- Sellers
- Administrators

The initial version of the system will support account management, clothing listings, product browsing, search and filtering, seller communication, reporting, and administrative management.

Physical delivery and direct financial transactions are outside the scope of the initial version.

---

### 1.3 Definitions and Abbreviations

- **UI:** User Interface
- **FR:** Functional Requirement
- **NFR:** Non-Functional Requirement
- **Admin:** Administrator
- **User Story:** A requirement written from the user's perspective
- **Sprint:** A fixed development period in Scrum

---

## 2. Overall System Description

### 2.1 Product Perspective

The system will be developed as a web-based application.

It will provide one organized platform where buyers and sellers can interact around pre-owned clothing listings, while administrators manage users, listings, and reported content.

---

### 2.2 User Roles

#### Buyer

A Buyer can:

- Register and log in
- Browse clothing listings
- Search and filter clothes
- View product details
- Save clothes
- Contact sellers
- Report inappropriate listings

#### Seller

A Seller can:

- Register and log in
- Create clothing listings
- Upload clothing images
- Add product information
- Edit listings
- View personal listings
- Mark items as sold
- Communicate with buyers

#### Administrator

An Administrator can:

- Manage registered users
- Monitor clothing listings
- Review reported listings
- Remove inappropriate content
- Access administrative functions

---

## 3. Functional Requirements

| ID | Functional Requirement |
| --- | --- |
| FR-001 | The system shall allow a user to create an account using valid information. |
| FR-002 | The system shall allow registered users to log in and log out securely. |
| FR-003 | The system shall display recently added clothing items. |
| FR-004 | The system shall allow users to browse clothes by category. |
| FR-005 | The system shall allow buyers to search for clothing items by name or keyword. |
| FR-006 | The system shall allow buyers to filter clothes by size and price. |
| FR-007 | The system shall display the condition of each clothing item. |
| FR-008 | The system shall allow sellers to upload images for clothing listings. |
| FR-009 | The system shall allow sellers to provide product information including price, size, condition, and description. |
| FR-010 | The system shall allow sellers to view their own clothing listings. |
| FR-011 | The system shall allow sellers to edit their own listings. |
| FR-012 | The system shall allow sellers to mark clothing items as sold. |
| FR-013 | The system shall allow buyers to save and remove favorite clothing items. |
| FR-014 | The system shall allow buyers to contact sellers regarding a specific clothing item. |
| FR-015 | The system shall allow users to report suspicious or inappropriate listings. |
| FR-016 | The system shall allow administrators to review reported listings. |
| FR-017 | The system shall allow administrators to manage registered users. |
| FR-018 | The system shall allow administrators to monitor the status of clothing listings. |
| FR-019 | The system shall generate notifications for relevant account activities. |
| FR-020 | The system shall support use on mobile, tablet, and desktop devices. |

---

## 4. Non-Functional Requirements

| ID | Non-Functional Requirement |
| --- | --- |
| NFR-001 | User passwords shall not be stored as plain text, and protected pages shall require authentication. |
| NFR-002 | Main pages shall respond within an acceptable time under normal system load. |
| NFR-003 | Forms shall validate required fields, formats, prices, and uploaded files. |
| NFR-004 | Administrative functions shall only be accessible to authorized administrators. |
| NFR-005 | User and product data shall be stored and retrieved reliably without unexpected loss. |
| NFR-006 | The website shall be tested on commonly used browsers including Chrome, Edge, and Firefox. |
| NFR-007 | The code shall be organized, documented, reviewed, and maintainable. |
| NFR-008 | The interface shall be simple and easy to navigate for users with basic computer skills. |

---

## 5. System Constraints

The initial version of the system will have the following constraints:

- The system will be developed as a web application.
- Physical delivery of clothing items will not be included.
- Direct online payment will not be included in the initial version.
- The system will depend on internet access.
- Administrative features will only be available to authorized administrators.
- The project must be completed and submitted by November 1, 2026.

---

## 6. Requirements Relationship to Product Backlog

The detailed User Stories, acceptance criteria, priorities, effort estimations, Sprint assignments, and responsible Developers are maintained in the Product Backlog.

This Requirements Specification defines what the system must provide, while the Product Backlog defines how the required work is organized and prioritized during Scrum development.

---

## 7. Requirement Review

The requirements will be reviewed throughout the project.

Changes may be made when:

- The team receives feedback.
- A requirement needs clarification.
- A technical issue is identified.
- The Product Owner changes the priority of a feature.
- The team identifies a better implementation approach.

Any important change should also be reflected in the Product Backlog.

---

## 8. Related Project Documents

- Project Overview
- Product Backlog
- Sprint Backlogs
- Use Case Diagram
- Sequence Diagrams
- Meeting Minutes

---

## PO Review and Approval

*Product Owner:* Sara Qateh  
*Review Date:* October 6, 2026  

*Approval Statement:*  
"I have reviewed this Software Requirements Specification and confirmed that it accurately reflects the current project goals, requirements, and Product Backlog. I approve this SRS as the basis for our Sprint planning and development work."

---

**Prepared by:** Project Team  
**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
