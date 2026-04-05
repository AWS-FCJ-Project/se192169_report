---
title: "Tuần 6: IaC & Container"
date: 2025-02-05
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 6:
* Xây dựng giao diện Dashboard cho Admin và Teacher.
* Tích hợp Tailwind CSS v4 để thiết kế giao diện hiện đại, tối giản.
* Đảm bảo tính phản hồi (Responsive) trên nhiều thiết bị.

### Các công việc cần triển khai trong tuần này:
|  | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| Thứ hai | - Tìm hiểu thêm về AWS CloudTrail<br>- Tìm hiểu AWS X-Ray | 09/02 | 09/02 | - |
| Thứ ba | - Terraform và cách chia module<br>- Phân tầng để quản lí tài nguyên/cấu hình | 10/02 | 10/02 | - |
| Thứ tư | - So sánh CloudFormation và Terraform<br>- Định hướng áp dụng cho project | 11/02 | 11/02 | - |
| Thứ năm | - Tạo branch cho phần hạ tầng dự án<br>- Dùng IaC tạo tài nguyên cơ bản (VPC, Security Group, EC2, NATGW)<br><strong>Khó khăn:</strong> chưa hiểu flow thực thi lệnh của Terraform | 12/02 | 12/02 | - |
| Thứ sáu | - Vẽ kiến trúc AWS cơ bản để deploy backend trên EC2 | 13/02 | 13/02 | - |
| Thứ bảy | - Cải thiện: chạy thử server backend trên EC2 bằng localhost<br>- Giám sát log server | 14/02 | 14/02 | - |
| Chủ Nhật | - Cài đặt backend trên 2 EC2 và chia traffic bằng ALB<br>- Tổng kết trước khi nghỉ Tết<br>- Xem thêm bài đăng kiến trúc AWS trên LinkedIn để lấy ý tưởng | 15/02 | 15/02 | - |

### Kết quả đạt được tuần 6:
* Hoàn thiện khung giao diện Dashboard chuyên nghiệp.
* Giao diện UI/UX mượt mà, hỗ trợ tốt chế độ sáng/tối (Dark Mode).
* Các tính năng quản lý cơ bản đã có thể thao tác trực tiếp trên màn hình.
* Chính sách bảo mật (IAM) được phân quyền chặt chẽ hơn.
