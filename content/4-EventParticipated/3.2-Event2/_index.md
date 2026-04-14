---
title: "Event 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---

# Report on "Cloud Mastery Series #2: DevOps Fundamentals & Infrastructure"

### Event Objectives

- Systematize knowledge about Infrastructure as Code and its practical implementation with Terraform on AWS.
- Master container orchestration by introducing Kubernetes architecture and modern application management in a cloud-native environment.
- Optimize operations with Elixir by exploring Elixir/Erlang as a unified tool for high-availability, fault-tolerant DevOps systems.
- Practice hands-on deployment techniques through live demonstrations.

### Speakers

- Thinh Nguyen - FCAJ Cloud Engineer Trainee, specialist in IaC and Terraform.
- Bao Huynh - Junior Cloud Native Developer at Endava and Founder of ITea Lab, specialist in Kubernetes.
- Nguyen Ta Minh Triet - R&D Member at ITea Lab and SAP Developer Intern at Bosch GSV, specialist in Elixir.

### Key Highlights

#### Infrastructure as Code with Terraform

- Analyzed the shift from ClickOps to infrastructure automation to reduce human error and improve consistency.
- Compared AWS CloudFormation, AWS CDK, and Terraform (HCL).
- Reviewed the workflow for managing state files and core execution commands such as plan, apply, and destroy.

#### Kubernetes Architecture

- Addressed the challenge of managing thousands of containers with self-healing and auto-scaling.
- Explored the core components: Control Plane, Worker Nodes, Pods, Deployments, and Services.
- Introduced supporting tools such as Helm for package management and K9s for a practical terminal interface.

#### Elixir in the DevOps Pipeline

- Highlighted the power of the BEAM virtual machine for handling millions of concurrent connections at very low cost.
- Learned the "let it crash" philosophy by using supervision trees to let systems recover automatically without manual intervention.
- Reviewed a case study where moving from Serverless (Node.js/Lambda) to Elixir reduced monthly cost from $30,000 to under $400.

### Outcomes

- Automation mindset: infrastructure is no longer a set of isolated servers, but code that can be versioned and reused.
- Efficient cluster management: understood that Amazon EKS is a strong option for reducing the operational burden of managing Kubernetes control planes.
- Fault tolerance: designing systems that can recover automatically is more important than trying to write code that never fails.
- Cost optimization: choosing the right technology, such as Elixir for parallel workloads, can deliver a much better ROI than traditional approaches.

### Application to Work

- Guide the EduTrust project: use Terraform to set up AWS infrastructure in a standardized way so environments can be reproduced more easily.
- Deploy applications: consider packaging EduTrust microservices into Docker and orchestrating them with Kubernetes for better availability.
- Improve performance: study event-driven architecture further through how Elixir manages processes and apply it to features that need real-time handling.

### Event Experience

The workshop provided a logical journey from infrastructure to application:

- Deep technical content: the Terraform and K9s demos made the practical operation of a cloud engineer much easier to visualize.
- A multi-angle perspective: combining popular technologies such as AWS and Kubernetes with high-performance Elixir expanded the way I think about solution selection.
- Strong networking value: the event created opportunities to exchange ideas with practitioners from companies such as Endava and Bosch.

### Lessons Learned

- Infrastructure modernization must go hand in hand with IaC to ensure speed and safety.
- Kubernetes is the "operating system" of the cloud, but supporting tools such as Helm and K9s are needed for effective administration.
- Do not hesitate to try newer languages or platforms if they solve cost and reliability problems better than common solutions.

### Conclusion

Cloud Mastery Series #2: DevOps Fundamentals & Infrastructure provided a solid knowledge base for modern DevOps practices. This foundation is important for building and operating EduTrust in a professional way, ready for larger-scale cloud problems.