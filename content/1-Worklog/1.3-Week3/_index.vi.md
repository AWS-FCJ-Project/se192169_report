---
title: "Tuần 3: S3, Identity & Monitoring"
date: 2025-01-15
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 3:
* Phân tích nghiệp vụ chi tiết cho nền tảng EduTrust.
* Thiết kế sơ đồ cơ sở dữ liệu NoSQL (MongoDB) và luồng xử lý AI.
* Hoàn thiện tài liệu SRS (Software Requirements Specification).

### Các công việc cần triển khai trong tuần này:
|  | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ hai | Tạo LinkedIn, tìm hiểu về S3 - S3 Glacier và các hình thức lưu trữ đảm bảo tối ưu chi phí | 19/01 | 19/01 | - |
| Thứ ba | File sharing và phân quyền truy cập S3 | 20/01 | 20/01 | - |
| Thứ tư | AWS Cognito cho xác thực, SSO (AWS Identity Center), AWS Organization | 21/01 | 21/01 | - |
| Thứ năm | ElastiCache Redis và RDS | 22/01 | 22/01 | - |
| Thứ sáu | AWS Cloudwatch và trực quan hóa log bằng Cloudwatch Alarm, AWS Grafana | 23/01 | 23/01 | - |
| Thứ bảy | Setup EC2 private subnet, dùng NATGW để kết nối Internet, pull container từ Docker về<br>Cài đặt Cloudwatch Agent vào EC2 để giám sát docker log | 24/01 | 24/01 | - |
| Chủ Nhật | Test thử tạo hạ tầng bằng Terraform qua các lệnh CLI | 25/01 | 25/01 | - |

### Kết quả đạt được tuần 3:
* Hoàn thiện khung kiến trúc EduTrust hướng tới khả năng mở rộng trên AWS.
* Tài liệu thiết kế hệ thống và Schema cơ sở dữ liệu đã sẵn sàng.
* Xác định rõ công nghệ sử dụng: FastAPI cho Backend và MongoDB cho Database.
