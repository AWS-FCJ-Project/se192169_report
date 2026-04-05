---
title: "Tuần 8: Packer & Hạ tầng backend"
date: 2025-03-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 8:
* Xây dựng module quản lý và báo cáo kết quả thi của sinh viên.
* Tích hợp dịch vụ gửi thông báo tự động (Amazon SES).
* Tối ưu hóa hiệu năng truy xuất dữ liệu từ MongoDB.

### Các công việc cần triển khai trong tuần này:
|  | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ hai | Áp dụng Packer để build AMI snapshot vào dự án | 02/03 | 02/03 | - |
| Thứ ba | Tìm hiểu về user data để đồng bộ version và package<br>- Triển khai endpoint cho S3, SSM, ECR,... | 03/03 | 03/03 | - |
| Thứ tư | Thiết kế lại CI/CD để tạo hạ tầng network và backend | 04/03 | 04/03 | - |
| Thứ năm | Thêm phần monitor bằng CloudWatch cho dự án | 05/03 | 05/03 | - |
| Thứ sáu | Ứng dụng user data và tối ưu package để tăng tốc độ CD | 06/03 | 06/03 | - |
| Thứ bảy | Tìm hiểu và dùng Route53 thay Cloudflare resolve DNS | 07/03 | 07/03 | - |
| Chủ Nhật | Chuẩn hóa và sửa lỗi hạ tầng backend, lựa chọn AMI checkpoint và cấu hình instance phù hợp | 08/03 | 08/03 | - |

### Kết quả đạt được tuần 8:
- Áp dụng Packer build AMI snapshot cho dự án.
- Nắm và áp dụng user data, triển khai endpoint cho S3/SSM/ECR.
- Thiết kế lại CI/CD để tạo hạ tầng network và backend.
- Bổ sung giám sát CloudWatch cho dự án.
- Tối ưu package để tăng tốc độ CD.
- Chuyển sang Route53 thay Cloudflare resolve DNS.
- Chuẩn hóa hạ tầng backend, chọn AMI checkpoint và cấu hình instance phù hợp.
