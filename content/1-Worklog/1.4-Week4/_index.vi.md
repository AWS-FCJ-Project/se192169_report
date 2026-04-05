---
title: "Tuần 4: ALB, IaC & CI/CD"
date: 2025-01-22
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 4:
* Xây dựng nền tảng Backend bằng FastAPI.
* Triển khai hệ thống xác thực người dùng (Authentication) qua JWT/Cognito.
* Kết nối và thực hiện các thao tác CRUD cơ bản trên MongoDB Atlas.

### Các công việc cần triển khai trong tuần này:
|  | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ hai | Dùng ALB để chia traffic tới các host, test connection từ client | 26/01 | 26/01 | - |
| Thứ ba | Vẽ mẫu kiến trúc để deploy một server backend và dùng IaC để build hạ tầng đã vẽ | 27/01 | 27/01 | - |
| Thứ tư | Tìm hiểu tiếp về CI/CD, hướng triển khai IaC trong CI/CD | 28/01 | 28/01 | - |
| Thứ năm | Chạy test hạ tầng tạo bằng IaC và deploy container bằng docker run | 29/01 | 29/01 | - |
| Thứ sáu | Brainstorm chủ đề project và tiêu chí chọn đề tài. | 30/01 | 30/01 | - |
| Thứ bảy | Chốt hướng chủ đề và phạm vi triển khai. | 31/01 | 31/01 | - |
| Chủ Nhật | Tìm hiểu thêm về các dịch vụ cho dự án (EC2-ASG, AWS ECR, DynamoDB, S3,...) | 01/02 | 01/02 | - |

### Kết quả đạt được tuần 4:
- Thiết lập ALB để chia traffic và kiểm thử kết nối từ client.
- Vẽ kiến trúc backend và triển khai hạ tầng theo IaC.
- Hiểu hướng triển khai IaC trong CI/CD và kiểm thử hạ tầng.
- Deploy container bằng `docker run` trên hạ tầng đã tạo.
- Chốt chủ đề, phạm vi dự án và khảo sát thêm các dịch vụ cần dùng (EC2-ASG, ECR, DynamoDB, S3,...).
