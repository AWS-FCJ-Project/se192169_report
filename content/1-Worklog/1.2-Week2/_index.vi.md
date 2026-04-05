---
title: "Tuần 2: EC2, Storage & IaC/CI-CD"
date: 2025-01-08
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 2:
* Làm quen các dịch vụ AWS Core cần thiết cho đồ án (IAM, EC2, S3).
* Cấu hình AWS CLI để quản trị tài nguyên qua dòng lệnh.
* Thử nghiệm lưu trữ và truy xuất tệp tin trên S3.

### Các công việc cần triển khai trong tuần này:
|  | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ hai | AWS CLI + Tiếp tục học về IaC | 12/01 | 12/01 | - |
| Thứ ba | AWS EC2 (AMI, Instance Type,...) + EFS/FSX + Lightsail | 13/01 | 13/01 | - |
| Thứ tư | EBS + User data + Metadata | 14/01 | 14/01 | - |
| Thứ năm | Auto Scaling Group (Lab tạo EC2 bằng ASG), Pricing option (On-demand, Reversed instance, Saving plans, Spot, ), Quản lí tài nguyên theo tag | 15/01 | 15/01 | - |
| Thứ sáu | Tìm hiểu về Terraform (basic cmd, cách hoạt động, lưu trữ state,...) | 16/01 | 16/01 | - |
| Thứ bảy | Lab về AWS EC2, Hosting Static Web using S3 + Cloudfront, cấu trúc CI/CD (Github Action, Jenkin,...) | 17/01 | 17/01 | - |
| Chủ Nhật | Ôn tập kiến thức, xem video hướng dẫn vẽ kiến trúc AWS, tiếp tục tìm hiểu CI/CD để giảm thiểu manual deploy | 18/01 | 18/01 | - |

### Kết quả đạt được tuần 2:
- Nắm vững thao tác AWS CLI và cách kết hợp với IaC.
- Hiểu các dịch vụ compute và storage: EC2 (AMI, Instance Type), EBS, EFS/FSx, Lightsail; kèm các khái niệm user data và metadata.
- Thực hành Auto Scaling Group, phân tích các lựa chọn chi phí (On-demand, Reserved Instance, Savings Plans, Spot) và quản lí tài nguyên theo tag.
- Nắm kiến thức Terraform cơ bản (command, cách hoạt động, state).
- Thực hành hosting Static Web trên S3 + CloudFront.
- Nắm tổng quan CI/CD (GitHub Actions, Jenkins) để giảm thao tác triển khai thủ công.
- Ôn tập và xem hướng dẫn vẽ kiến trúc AWS, hệ thống lại kiến thức đã học.
