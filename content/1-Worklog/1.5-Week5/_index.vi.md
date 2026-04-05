---
title: "Tuần 5: ECR, Monitoring & WAF"
date: 2025-01-29
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 5:
* Nghiên cứu tích hợp mô hình YOLO để giám sát camera phòng thi.
* Thiết kế kiến trúc AI Agentic Workflow cho chatbot hỗ trợ học tập.
* Thực hiện thử nghiệm nhận diện vật thể cơ bản (điện thoại, khuôn mặt).

### Các công việc cần triển khai trong tuần này:
|  | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ hai | Ứng dụng ECR trong việc tạo repo và lưu trữ image<br><strong>Ý tưởng:</strong> Dùng ECR để lưu trữ backend image sau khi được docker đóng gói | 02/02 | 02/02 | - |
| Thứ ba | Thiết lập CloudWatch log management, alarm và metrics, Security Hub | 03/02 | 03/02 | - |
| Thứ tư | Tìm hiểu về WAF để bảo vệ tầng Application | 04/02 | 04/02 | - |
| Thứ năm | Brainstorm lại topic project và kiến trúc dự án | 05/02 | 05/02 | - |
| Thứ sáu | Tìm hiểu Kiro, MCP và Kiro-CLI - Gợi ý kiến trúc dự án dựa trên source code | 06/02 | 06/02 | - |
| Thứ bảy | Ôn tập kiến thức cơ bản về VPC, EC2, CloudWatch và IaC, CI/CD | 07/02 | 07/02 | - |
| Chủ Nhật | Tìm hiểu về cơ chế Instance Refresh của ASG<br><strong>Ý tưởng:</strong> Dùng Instance Refresh để đồng bộ versioning giữa các host mỗi khi có update | 08/02 | 08/02 | - |

### Kết quả đạt được tuần 5:
- Ứng dụng ECR để tạo repo và lưu trữ image cho backend.
- Thiết lập CloudWatch log management, alarm/metrics và Security Hub.
- Nắm vai trò của WAF trong bảo vệ tầng ứng dụng.
- Brainstorm lại topic và kiến trúc dự án theo hướng phù hợp.
- Tìm hiểu Kiro, MCP, Kiro-CLI để gợi ý kiến trúc từ source code.
- Ôn tập VPC, EC2, CloudWatch, IaC, CI/CD.
- Hiểu cơ chế Instance Refresh của ASG và định hướng áp dụng đồng bộ versioning.
