---
title: "Event 3"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Report on "Cloud Mastery Series #3: Security"

This workshop focused on practical AWS security, from networking and IAM to advanced defense layers.

### Event Objectives

- Implement AWS networking security configurations such as SG, NACL, VPC, CIDR, Subnet, IGW, and VPC Endpoint.
- Build AWS accounts and manage users with AWS IAM, introducing SCP, Permission Boundary, Credential Rotation, and user policy/rule constraints.
- Optimize AWS firewall services such as WAF, Shield, Network Firewall, and Firewall Manager.
- Demonstrate infrastructure and application deployment techniques through live demos and video sessions.

### Speakers

- Lam An Thinh - DataXight Security Engineer Intern.
- Nguyen Phan Quoc Viet - DevOps Engineer.
- Huynh Hoang Long - FCAJ Cloud Engineer Ambassador.
- Dang Thi Minh Thu - FCAJ Cloud Engineer Ambassador.

### Key Highlights

#### AWS Network Security

- VPC helps isolate resources by environment and network boundary.
- Security Group and Network ACL complement each other at the Instance and Subnet levels.
- CIDR and Subnet planning make the network layout scalable and easier to maintain.
- Internet Gateway and VPC Endpoint control traffic paths between private resources and AWS services.

#### Identity and Access Management

- AWS IAM structures users, groups, roles, and policies in a clear way.
- SCP and Permission Boundary limit permissions at the organization and Identity levels.
- Credential Rotation reduces the risk of leaked access credentials.
- Least Privilege keeps access limited to what is actually needed.

#### Advanced Firewall Layers

- AWS WAF filters malicious traffic at the application layer.
- AWS Shield improves resilience against DDoS attacks.
- Network Firewall provides more flexible network-level traffic control.
- Firewall Manager centralizes security policy management across multiple accounts and services.

### Outcomes

- AWS security should be designed in layers rather than relying on a single tool.
- IAM, SCP, and Permission Boundary form a critical trio for access control.
- Strong network design from the start reduces misconfiguration and future security risk.
- WAF, Shield, and Network Firewall should be treated as part of the operational architecture.

### Application to Work

- Apply a clearer network segmentation mindset to the EduTrust project to organize resources, Subnets, and access flows more cleanly.
- Review user, role, and policy management more carefully to reduce AWS operational risk.
- Consider adding protection layers at both the application and network levels for public-facing services.
- Build the habit of reviewing access permissions and rotating credentials on a regular schedule.

### Event Experience

The workshop gave a practical view of cloud security:

- The demos made each security layer easier to understand.
- Combining Networking, Identity Management, and Firewall concepts made the overall picture more complete.
- The examples map well to real infrastructure deployment challenges.

### Lessons Learned

- Security should be designed from the start, not added later.
- Access should follow Least Privilege and be controlled through multiple layers.
- Private networking, segmentation, and access governance are the foundation of a secure AWS system.
- Automation and policy standardization reduce human error and improve consistency.

### Conclusion

Cloud Mastery Series #3: Security provided a practical foundation for securing AWS environments, from Networking and IAM to advanced defense layers. These lessons are an important base for safer, more controlled, and more scalable design practices in EduTrust.