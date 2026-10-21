# Sprint 3 Review and Retrospective

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Meeting Type:** Sprint Review and Sprint Retrospective  
**Sprint:** Sprint 3  
**Date:** October 21, 2026  
**Duration:** Approximately 23 minutes  
**Platform:** Google Meet / Recorded  
**Total Story Points:** 29  

---

## 👥 Attendees

| Name | Role | Attendance |
|---|---|---|
| Hajar Khawari | Scrum Master | Present |
| Sara Qateh | Product Owner | Present |
| Nargis Bunyadi | Developer | Present |
| Parwana Jafari | Developer | Present |

---

# Sprint Review

## 🎯 Sprint Goal

The goal of Sprint 3 was to give sellers more control over their listings and allow buyers to save clothes and communicate with sellers.

The Sprint 3 backlog included:

▪ US-010 – View My Listings  
▪ US-011 – Edit Listing  
▪ US-012 – Mark as Sold  
▪ US-013 – Save Clothes  
▪ US-014 – Contact Seller  
▪ NFR-005 – Data Reliability  

A total of **29 Story Points** were planned for Sprint 3.

---

## 💻 Sprint 3 Demonstration

Nargis and Parwana demonstrated the completed Sprint 3 work during the meeting.

---

### 👩‍💻 Nargis Bunyadi – Frontend Demonstration

Nargis explained the frontend work completed for Sprint 3.

She worked on:

▪ Edit Listing interface  
▪ Mark as Sold interface  
▪ Contact Seller form  
▪ Inbox page  
▪ Contact Seller link on product cards  
▪ Inbox link in the account menu  
▪ Validation for empty messages  
▪ Loading, success, and error messages  

For **Edit Listing**, sellers can update:

▪ Clothing name  
▪ Category  
▪ Price  
▪ Size  
▪ Condition  
▪ City  
▪ Description  

Sellers can also keep the current photo or choose a replacement photo.

For **Mark as Sold**, Nargis added:

▪ A confirmation message  
▪ Updated status display  
▪ Available and Sold labels  
▪ Improved button behavior during requests  

She also explained that the frontend changes needed to be tested together with the backend.

---

### 👩‍💻 Parwana Jafari – Backend and System Demonstration

Parwana shared her screen and demonstrated how the Sprint 3 features work in the actual system.

She first showed the **Seller Dashboard**.

When a seller logs in, the dashboard displays the clothing listings created by that seller.

From the dashboard, the seller can:

▪ View their own listings  
▪ Add a new listing  
▪ Edit an existing listing  
▪ View the current listing status  

Parwana then demonstrated the **Edit Listing** feature.

She changed information in an existing clothing listing and showed that the seller can update listing details.

The photo replacement is optional, so the seller can keep the current photo or choose a new one.

After saving the changes, the updated information was displayed successfully.

She then demonstrated the **Mark as Sold** feature.

The product was first shown as **Available**.

After selecting Mark as Sold and confirming the action, the status changed to **Sold**.

Parwana returned to the listings and showed that the updated status and edited information were saved correctly.

She also checked the Homepage and showed that the listing status was updated there as well.

Finally, Parwana demonstrated the **Contact Seller and Inbox** functionality.

She:

▪ Opened a clothing listing  
▪ Selected Contact Seller  
▪ Wrote a message to the seller  
▪ Sent the message successfully  
▪ Logged out from the buyer account  
▪ Logged in with another user account  
▪ Opened the seller Inbox  
▪ Confirmed that the new message was received correctly  

The Inbox displayed the message together with the related clothing item and message information.

This demonstration confirmed that the buyer-to-seller messaging flow was working correctly.

---

## ✅ Testing Confirmation

During the Sprint Review, the team confirmed that the main Sprint 3 features had been tested together.

The developers reported that the features were working correctly.

The team confirmed that all planned **29 Story Points** for Sprint 3 were completed.

---

## 💡 Product Decision – Listing Availability

During the Sprint Review, the team discussed how a seller should handle a listing that they no longer want to sell.

Instead of completely deleting the product from the system, the Product Owner suggested changing its status to:

**Not Available**

This allows the listing to remain in the seller's account and gives the seller the option to make it available again in the future.

The team agreed that this approach is better than permanently deleting the product.

---

## 👩‍💼 Product Owner Feedback

Sara reviewed the Sprint 3 work and gave positive feedback.

She especially liked:

▪ The clean and easy-to-understand Seller Dashboard  
▪ The user-friendly listing management interface  
▪ The option to add new clothing listings  
▪ The messaging and Inbox functionality  
▪ Direct communication between buyers and sellers  
▪ The overall design of the marketplace  

Sara also explained that the messaging feature is useful because buyers may have questions about size, product details, or other information before making a decision.

She appreciated the developers' work and teamwork.

---

## 📊 Sprint 3 Final Status

| Metric | Result |
|---|---:|
| Story Points Planned | 29 |
| Story Points Completed | 29 |
| Remaining Story Points | 0 |
| Completion Rate | 100% |
| Main Features Tested | Yes |
| Product Owner Acceptance | Accepted |
| Sprint Goal | Achieved |
| Sprint Status | ✅ Completed |

---

## ✅ Sprint Review Result

Sprint 3 was reviewed and accepted by the Product Owner.

All 29 planned Story Points were completed.

The Sprint Goal was achieved.

---

# Sprint Retrospective

## 🎯 Retrospective Purpose

After the Sprint Review, the team discussed their experience during Sprint 3.

The discussion focused on:

▪ What was good during the Sprint  
▪ What was difficult  
▪ What the team learned from the work  

---

## 👩‍💻 Parwana Jafari

Parwana explained that her backend work included creating routes, connecting functionality, and testing the system.

She said the work generally went well, but she faced some small technical issues.

Some problems were caused by small differences in names, file references, or connected parts of the system.

Even a small naming difference could stop one part from connecting correctly with another part.

She solved these issues by checking the code carefully, finding the mismatch, and correcting it.

---

## 👩‍💻 Nargis Bunyadi

Nargis said Sprint 3 was a good experience, but some parts were difficult because there was more code and more functionality to manage.

She explained that working with many parts at the same time could sometimes be confusing.

However, she continued working through the problems and completed her frontend work.

---

## 👩‍💼 Sara Qateh

Sara thanked the developers for their hard work.

She recognized that Sprint 3 included a lot of development work and appreciated the effort of the team.

She also explained that her suggestions and feedback are meant to improve the product and make it better for users.

---

## ⚠️ Challenges Discussed

The team discussed several challenges during Sprint 3:

▪ Managing a larger amount of code  
▪ Finding errors when functionality did not work as expected  
▪ Small naming differences between connected parts  
▪ Rechecking code several times to find simple but important problems  
▪ Frontend and backend integration  

The developers were able to solve the issues and demonstrate the working Sprint 3 features.

---

## 📌 Lessons from Sprint 3

The team learned that:

▪ Small naming differences can cause important integration problems  
▪ Frontend and backend connections should be checked carefully  
▪ Testing helps find problems before the final demonstration  
▪ Complex work is easier when it is checked step by step  
▪ Clear communication helps the team solve problems faster  

---

## 🏁 Sprint 3 Outcome

Sprint 3 was completed successfully.

The team completed all 29 planned Story Points and demonstrated the main listing-management and communication features.

The Product Owner reviewed the final result and accepted the Sprint.

The team will use the experience and lessons from Sprint 3 while moving into Sprint 4.

---

## 🎥 Recording

**Recording Link:** https://drive.google.com/file/d/1cUFiBQX_vSx773RWQ2QHfHab4Jk2Hd04/view?usp=sharing  

---

## Document Information

**Document Prepared by:** Hajar Khawari (Scrum Master)  
**Approved by:** Sara Qateh (Product Owner)
