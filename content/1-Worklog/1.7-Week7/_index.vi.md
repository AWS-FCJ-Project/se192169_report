---
title: "Tuần 7: Hạ tầng & CI/CD"
date: 2025-02-23
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 7:
* Thiết lập hạ tầng mạng VPC/EC2 cho hệ thống EduTrust.
* Triển khai hạ tầng dưới dạng mã (Infrastructure as Code - IaC).
* Cấu hình cân bằng tải (Load Balancer) và bảo mật SSL/HTTPS.

### Các công việc cần triển khai trong tuần này:
|  | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ hai | IaC dựng hạ tầng ASG, cấu hình Cloudflare resolve DNS và TLS cert cho domain | 23/02 | 23/02 | - |
| Thứ ba | Cấu hình Security Group, Health Check, scale in/out cho ASG | 24/02 | 24/02 | - |
| Thứ tư | Xây dựng CI/CD cơ bản cho dự án | 25/02 | 25/02 | - |
| Thứ năm | Tìm hiểu Packer để lưu snapshot AMI tạo Launch Template cho ASG (đồng bộ phiên bản gói cài đặt) | 26/02 | 26/02 | - |
| Thứ sáu | Chạy thử hạ tầng Terraform trong CI/CD, sửa lỗi khi commit và chạy pipeline | 27/02 | 27/02 | - |
| Thứ bảy | Cập nhật kiến trúc AWS của dự án, cải thiện CI, phân job rõ ràng cho CD | 28/02 | 28/02 | - |
| Chủ Nhật | Báo cáo, cập nhật dự án cho nhóm | 01/03 | 01/03 | - |

### Kết quả đạt được tuần 7:
- Dựng hạ tầng ASG bằng IaC và cấu hình DNS/TLS cho domain.
- Thiết lập Security Group, Health Check và scale in/out cho ASG.
- Xây dựng CI/CD cơ bản và chạy Terraform trong pipeline.
- Ứng dụng Packer tạo AMI, Launch Template đồng bộ package.
- Cập nhật kiến trúc AWS, cải thiện CI và phân job rõ ràng cho CD.
- Báo cáo tiến độ và cập nhật dự án cho nhóm.
