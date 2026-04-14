---
title: "Event 3"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Bài Thu Hoạch “Cloud Mastery Series #3: Security”

Buổi workshop này tập trung vào bảo mật AWS theo hướng thực hành, từ Networking, IAM cho đến các lớp phòng thủ nâng cao.

### Mục Tiêu Sự Kiện

- Triển khai các cấu hình bảo mật liên quan đến Networking trên AWS như SG, NACL, VPC, CIDR, Subnet, IGW, VPC Endpoint,...
- Xây dựng tài khoản AWS và quản lí user với AWS IAM, giới thiệu về SCP, Permission Boundary, Credential Rotation và các chính sách quản lí, ràng buộc policy/rule cho user.
- Tối ưu các dịch vụ tường lửa trên AWS như WAF, Shield, Network Firewall và Firewall Manager.
- Thực hành thực tế (Hands-on) qua Demo trực tiếp và Video.

### Diễn Giả

- Lâm An Thịnh - DataXight Security Engineer Intern.
- Nguyễn Phan Quốc Việt - DevOps Engineer.
- Huỳnh Hoàng Long - FCAJ Cloud Engineer Ambassador.
- Đặng Thị Minh Thư - FCAJ Cloud Engineer Ambassador.

### Điểm Nổi Bật

#### Bảo Mật Mạng Trên AWS

- VPC giúp cô lập tài nguyên theo từng môi trường và từng vùng mạng riêng.
- Security Group và Network ACL bổ sung cho nhau trong việc kiểm soát truy cập ở cấp Instance và Subnet.
- CIDR và Subnet giúp thiết kế dải mạng hợp lý, dễ mở rộng và dễ quản trị.
- Internet Gateway và VPC Endpoint giúp kiểm soát luồng truy cập giữa private resources và dịch vụ AWS.

#### Quản Lí Danh Tính Và Quyền Truy Cập Với IAM

- AWS IAM hỗ trợ quản lý user, group, role và policy theo cấu trúc rõ ràng.
- SCP và Permission Boundary giúp giới hạn quyền ở cấp tổ chức và cấp Identity.
- Credential Rotation là bước quan trọng để giảm rủi ro lộ thông tin truy cập.
- Tư duy Least Privilege giúp cấp quyền đúng mức cần thiết, không dư thừa.

#### Tường Lửa Và Lớp Phòng Thủ Nâng Cao

- AWS WAF hỗ trợ lọc lưu lượng độc hại ở tầng ứng dụng.
- AWS Shield tăng khả năng chống chịu trước các cuộc tấn công DDoS.
- Network Firewall cho phép kiểm soát lưu lượng ở cấp mạng linh hoạt hơn.
- Firewall Manager giúp quản trị tập trung các chính sách bảo mật trên nhiều tài khoản và dịch vụ.

### Kết Quả Rút Ra

- Bảo mật trên AWS nên được thiết kế theo nhiều lớp, không phụ thuộc vào một công cụ đơn lẻ.
- IAM, SCP và Permission Boundary là bộ ba quan trọng trong kiểm soát quyền truy cập.
- Thiết kế mạng tốt ngay từ đầu giúp giảm lỗi cấu hình và rủi ro bảo mật về sau.
- WAF, Shield và Network Firewall nên được xem là một phần của kiến trúc vận hành.

### Ứng Dụng Vào Công Việc

- Áp dụng tư duy phân tách mạng rõ ràng hơn cho dự án EduTrust để tổ chức tài nguyên, Subnet và luồng truy cập hợp lý.
- Xem xét quy trình quản lý user, role và policy chặt chẽ hơn để giảm rủi ro trong vận hành AWS.
- Cân nhắc bổ sung các lớp phòng thủ ở tầng ứng dụng và tầng mạng cho các dịch vụ public-facing.
- Tăng cường thói quen rà soát quyền truy cập và xoay vòng Credential theo định kỳ.

### Trải Nghiệm Sự Kiện

Buổi workshop mang lại góc nhìn thực tế về bảo mật Cloud:

- Nội dung có chiều sâu, giúp hình dung rõ cách cấu hình và vận hành các lớp bảo mật trên AWS.
- Kết hợp Networking, Identity Management và Firewall để tạo thành bức tranh bảo mật hoàn chỉnh hơn.
- Nhiều ví dụ có thể liên hệ trực tiếp với các bài toán triển khai hạ tầng trong dự án thực tế.

### Bài Học Rút Ra

- Bảo mật cần được thiết kế từ đầu, không nên đợi đến khi hệ thống chạy rồi mới bổ sung.
- Quyền truy cập nên được cấp theo nguyên tắc tối thiểu cần thiết và được kiểm soát nhiều lớp.
- Mạng riêng, phân vùng hợp lý và quản trị truy cập tốt là nền tảng cho một hệ thống AWS an toàn, bền vững.
- Tự động hóa và tiêu chuẩn hóa policy giúp giảm lỗi con người và tăng tính nhất quán khi mở rộng hệ thống.

### Tổng Kết

Cloud Mastery Series #3: Security đã cung cấp một nền tảng thực tế về bảo mật trên AWS, từ Networking, IAM đến các lớp phòng thủ nâng cao. Những kiến thức này là cơ sở quan trọng để em áp dụng vào việc thiết kế và vận hành hệ thống EduTrust an toàn hơn, có kiểm soát hơn và sẵn sàng mở rộng trong tương lai.