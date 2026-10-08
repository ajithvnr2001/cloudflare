---
url: https://blog.cloudflare.com/vi-vn/code-mode-mcp/
title: Ch\u1ebf \u0111\u1ed9 M\u00e3: n\u00e9n to\u00e0n b\u1ed9 API v\u00e0o 1.000 m\u00e3 th\u00f4ng b\u00e1o \u0111\u1ec3 t\u00e1c nh\u00e2n khai th\u00e1c | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:40:54.655469+00:00
---

# Chế độ Mã: nén toàn bộ API vào 1.000 mã thông báo để tác nhân khai thác | Blog Cloudflare

> Source: https://blog.cloudflare.com/vi-vn/code-mode-mcp/

[Blog](https://blog.cloudflare.com/vi-vn/)

[AI](https://blog.cloudflare.com/vi-vn/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/vi-vn/tag/workers/)[Nền tảng Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developer-platform/)+4Hiển thị thêm 4 thẻ

7 thẻHiển thị 7 thẻ

  * Thẻ bài viết
  * [AI](https://blog.cloudflare.com/vi-vn/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/vi-vn/tag/workers/)[Nền tảng Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developer-platform/)[Nguồn mở](https://blog.cloudflare.com/vi-vn/tag/open-source/)[Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developers/)[Tối ưu hóa](https://blog.cloudflare.com/vi-vn/tag/optimization/)[Workers AI](https://blog.cloudflare.com/vi-vn/tag/workers-ai/)
  * Tất cả thẻ
  * Thẻ phù hợp
  * Không tìm thấy thẻ nào
  * [AI](https://blog.cloudflare.com/vi-vn/tag/ai/)
  * [Các Bot AI](https://blog.cloudflare.com/vi-vn/tag/ai-bots/)
  * [Birthday Week](https://blog.cloudflare.com/vi-vn/tag/birthday-week/)
  * [Quản lý bot](https://blog.cloudflare.com/vi-vn/tag/bot-management/)
  * [Tuyển dụng](https://blog.cloudflare.com/vi-vn/tag/careers/)
  * [Cloudflare One](https://blog.cloudflare.com/vi-vn/tag/cloudflare-one/)
  * [Cloudflare Stream](https://blog.cloudflare.com/vi-vn/tag/cloudflare-stream/)
  * [Cloudflare Workers](https://blog.cloudflare.com/vi-vn/tag/workers/)
  * [Mã hóa](https://blog.cloudflare.com/vi-vn/tag/cryptography/)
  * [Nền tảng Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developer-platform/)
  * [Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developers/)
  * [Google](https://blog.cloudflare.com/vi-vn/tag/google/)
  * [Tác động](https://blog.cloudflare.com/vi-vn/tag/impact/)
  * [Trải nghiệm Thực tập](https://blog.cloudflare.com/vi-vn/tag/internship-experience/)
  * [Ipsec](https://blog.cloudflare.com/vi-vn/tag/ipsec/)
  * [Pháp lý](https://blog.cloudflare.com/vi-vn/tag/legal/)
  * [Cuộc sống tại Cloudflare](https://blog.cloudflare.com/vi-vn/tag/life-at-cloudflare/)
  * [Nguồn mở](https://blog.cloudflare.com/vi-vn/tag/open-source/)
  * [Tối ưu hóa](https://blog.cloudflare.com/vi-vn/tag/optimization/)
  * [Đối tác](https://blog.cloudflare.com/vi-vn/tag/partners/)
  * [Chính sách và Pháp lý](https://blog.cloudflare.com/vi-vn/tag/policy/)
  * [Hậu lượng tử](https://blog.cloudflare.com/vi-vn/tag/post-quantum/)
  * [Tin tức về sản phẩm](https://blog.cloudflare.com/vi-vn/tag/product-news/)
  * [Dự án Galileo](https://blog.cloudflare.com/vi-vn/tag/project-galileo/)
  * [Radar](https://blog.cloudflare.com/vi-vn/tag/cloudflare-radar/)
  * [Bảo mật](https://blog.cloudflare.com/vi-vn/tag/security/)
  * [Tốc độ](https://blog.cloudflare.com/vi-vn/tag/speed/)
  * [Tốc độ và Độ tin cậy](https://blog.cloudflare.com/vi-vn/tag/speed-and-reliability/)
  * [Workers AI](https://blog.cloudflare.com/vi-vn/tag/workers-ai/)
  * [Zero Trust](https://blog.cloudflare.com/vi-vn/tag/zero-trust/)



[Nguồn mở](https://blog.cloudflare.com/vi-vn/tag/open-source/)[Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developers/)[Tối ưu hóa](https://blog.cloudflare.com/vi-vn/tag/optimization/)[Workers AI](https://blog.cloudflare.com/vi-vn/tag/workers-ai/)

[AI](https://blog.cloudflare.com/vi-vn/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/vi-vn/tag/workers/)[Nền tảng Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developer-platform/)[Nguồn mở](https://blog.cloudflare.com/vi-vn/tag/open-source/)[Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developers/)[Tối ưu hóa](https://blog.cloudflare.com/vi-vn/tag/optimization/)[Workers AI](https://blog.cloudflare.com/vi-vn/tag/workers-ai/)

20 tháng 2, 2026

# Chế độ Mã: cung cấp toàn bộ APIcho tác nhân AItrong giới hạn 1.000 mã thông báo

![Matt Carey](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BHQSGCBKVGAAVQVS4V3E.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Carey](https://blog.cloudflare.com/vi-vn/author/matt-carey/)

Cần 12 phút để đọc

SAO CHÉP URL

Bài viết này cũng có sẵn bằng [English](https://blog.cloudflare.com/code-mode-mcp/), [Italiano](https://blog.cloudflare.com/it-it/code-mode-mcp/), [日本語](https://blog.cloudflare.com/ja-jp/code-mode-mcp/), [한국어](https://blog.cloudflare.com/ko-kr/code-mode-mcp/), [繁體中文](https://blog.cloudflare.com/zh-tw/code-mode-mcp/) và [简体中文](https://blog.cloudflare.com/zh-cn/code-mode-mcp/).

![images/BLOG-3184 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487D5XYR4AZJYHJN5AX56Q.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9/T06+rs5+nv6e317e/07uzt////+/r/5ubz0tbpytPs0Nvz2eHz3uPs/v//8vT/09nzs8Dop7zqs8jyxNXzztvt////8fb/zNb2pLjrl7TtqcT1v9T2y9vw/////P//1+H8ssfyq8X1vtX80eL82ef1////////7PP/0OH80OL/4e//7fj/7/j7/////////v//6fb/7fr//P//////////////////////8///+P//////////////)

[_Giao thức Ngữ cảnh Mô hình_](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) (Model Context Protocol, MCP) đã trở thành phương thức tiêu chuẩn để các tác nhân AI sử dụng các công cụ bên ngoài. Tuy nhiên, ngay ở cốt lõi vẫn tồn tại một mâu thuẫn: các tác nhân cần nhiều công cụ để thực hiện công việc hiệu quả, nhưng mỗi công cụ được bổ sung đều chiếm dung lượng cửa sổ ngữ cảnh của mô hình, làm giảm không gian dành cho nhiệm vụ chính. 

[_Chế độ Mã_](https://blog.cloudflare.com/code-mode/) (Code Mode) là kỹ thuật chúng tôi lần đầu giới thiệu nhằm giảm thiểu việc sử dụng cửa sổ ngữ cảnh trong quá trình tác nhân sử dụng công cụ. Thay vì mô tả mỗi thao tác như một công cụ riêng biệt, hãy để mô hình viết mã dựa trên một SDK có định kiểu và thực thi mã một cách an toàn trong [_Dynamic Worker Loader_](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/). Mã này đóng vai trò như một kế hoạch gọn nhẹ. Mô hình này có thể khám phá các thao tác của công cụ, kết hợp nhiều lệnh gọi và chỉ trả về dữ liệu cần thiết. Anthropic đã độc lập nghiên cứu mô hình tương tự trong một bài viết có tiêu đề [_Code Execution with MCP_](https://www.anthropic.com/engineering/code-execution-with-mcp) (Thực thi mã với MCP).

Hôm nay, chúng tôi ra mắt [_một máy chủ MCP mới_](https://github.com/cloudflare/mcp) cho [_toàn bộ hệ sinh thái API của Cloudflare_](https://developers.cloudflare.com/api/) \- từ [_DNS_](https://developers.cloudflare.com/dns/) và [_Zero Trust_](https://developers.cloudflare.com/cloudflare-one/) đến [_Workers_](https://workers.cloudflare.com/product/workers/) và [_R2_](https://workers.cloudflare.com/product/r2/) \- sử dụng Chế độ Mã. Chỉ với hai công cụ, search() và execute(), máy chủ có thể cung cấp quyền truy cập vào toàn bộ API của Cloudflare thông qua MCP mà chỉ tiêu tốn khoảng 1.000 mã thông báo. Dấu vết hoạt động không thay đổi, bất kể có bao nhiêu điểm cuối API.

Đối với một API lớn như API của Cloudflare, Chế độ Mã có thể giảm 99,9% lượng mã thông báo đầu vào cần dùng. Một máy chủ MCP tương đương khi không có Chế độ Mã sẽ tiêu tốn 1,17 triệu mã thông báo — nhiều hơn toàn bộ cửa sổ ngữ cảnh của các mô hình nền tảng tiên tiến nhất.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![images/BLOG-3184 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48S1W1QET0HW2VBF96B97E.png&w=715&h=179&f=webp&fit=cover&position=center)

_Mức tiết kiệm khi sử dụng Chế độ Mã so với MCP gốc, được đo bằng[ _thư viện tiktoken_](https://github.com/openai/tiktoken)_

Bạn có thể bắt đầu sử dụng máy chủ MCP mới của Cloudflare này ngay hôm nay. Và chúng tôi cũng đang công khai mã nguồn một [_SDK Chế độ Mã_](https://github.com/cloudflare/agents/tree/main/packages/codemode) mới trong [_SDK cho Tác nhân của Cloudflare_](https://github.com/cloudflare/agents) để bạn có thể sử dụng cùng một phương pháp trong các máy chủ MCP và Tác nhân AI của riêng mình.

### Chế độ Mã phía máy chủ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![images/BLOG-3184 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GDDXDC3J77QYJRE40PVA.png&w=715&h=446&f=webp&fit=cover&position=center)

Máy chủ MCP mới này áp dụng Chế độ Mã ở phía máy chủ. Thay vì hàng ngàn công cụ, máy chủ chỉ xuất ra hai công cụ: `search()` và `execute()`. Cả hai đều được vận hành bởi Chế độ Mã. Dưới đây là toàn bộ phạm vi công cụ được tải vào ngữ cảnh của mô hình:
    
    
    [
      {
        "name": "search",
        "description": "Search the Cloudflare OpenAPI spec. All $refs are pre-resolved inline.",
        "inputSchema": {
          "type": "object",
          "properties": {
            "code": {
              "type": "string",
              "description": "JavaScript async arrow function to search the OpenAPI spec"
            }
          },
          "required": ["code"]
        }
      },
      {
        "name": "execute",
        "description": "Execute JavaScript code against the Cloudflare API.",
        "inputSchema": {
          "type": "object",
          "properties": {
            "code": {
              "type": "string",
              "description": "JavaScript async arrow function to execute"
            }
          },
          "required": ["code"]
        }
      }
    ]
    

Để khám phá các khả năng của chính mình, tác nhân sẽ gọi hàm `search()`. Nó viết mã JavaScript dựa trên một biểu diễn có định kiểu đối với đặc tả OpenAPI. Tác nhân này có thể lọc các điểm cuối theo sản phẩm, đường dẫn, thẻ hoặc bất kỳ siêu dữ liệu nào khác và thu hẹp hàng nghìn điểm cuối xuống còn một số ít điểm cuối cần thiết. Toàn bộ đặc tả OpenAPI sẽ không bao giờ được đưa vào ngữ cảnh của mô hình. Tác nhân chỉ tương tác với nó thông qua mã.

Khi tác nhân sẵn sàng hành động, nó sẽ gọi hàm `execute()`. Tác nhân này viết mã có khả năng gửi yêu cầu tới API của Cloudflare, xử lý phân trang, kiểm tra phản hồi và chuỗi hoá các thao tác trong một lần thực thi duy nhất. 

Cả hai công cụ đều chạy mã được tạo ra bên trong môi trường [_Dynamic Worker_](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) biệt lập - một môi trường hộp cát (sandbox) V8 nhẹ, không có hệ thống tập tin, không có biến môi trường bị rò rỉ thông qua chèn lệnh nhắc và việc tải về từ bên ngoài bị vô hiệu hóa mặc định. Các yêu cầu gửi đi có thể được kiểm soát rõ ràng bằng các trình xử lý tìm nạp gửi đi khi cần thiết.

#### Ví dụ: Bảo vệ máy chủ gốc khỏi các cuộc tấn công DDoS

Giả sử người dùng yêu cầu tác nhân của họ: "bảo vệ máy chủ gốc của tôi khỏi các cuộc tấn công DDoS." Bước đầu tiên mà tác nhân thực hiện là tham khảo tài liệu. Nó có thể gọi đến [_máy chủ MCP của Tài liệu Cloudflare_](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/), sử dụng một [_Kỹ năng của Cloudflare_](https://github.com/cloudflare/skills), hoặc tìm kiếm trực tiếp trên web. Theo tài liệu hướng dẫn, tác nhân biết rằng cần đặt ra các quy tắc [_Cloudflare WAF_](https://www.cloudflare.com/application-services/products/waf/) và quy tắc [_bảo vệ chống lại DDoS_](https://www.cloudflare.com/ddos/) phía trước máy chủ gốc.

**Bước 1: Tìm kiếm các điểm cuối phù hợp  
** Công cụ `tìm kiếm` cung cấp cho mô hình một đối tượng `đặc tả` : toàn bộ đặc tả OpenAPI của Cloudflare trong đó tất cả các tham chiếu `$refs` đã đượcxử lý sẵn. Mô hình này viết mã JavaScript dựa trên đó. Tại đây, tác nhân sẽ tìm kiếm các điểm cuối WAF và bộ quy tắc trên một vùng:
    
    
    async () => {
      const results = [];
      for (const [path, methods] of Object.entries(spec.paths)) {
        if (path.includes('/zones/') &&
            (path.includes('firewall/waf') || path.includes('rulesets'))) {
          for (const [method, op] of Object.entries(methods)) {
            results.push({ method: method.toUpperCase(), path, summary: op.summary });
          }
        }
      }
      return results;
    }
    

Máy chủ chạy đoạn mã này trong môi trường Workers biệt lập và trả về:
    
    
    [
      { "method": "GET",    "path": "/zones/{zone_id}/firewall/waf/packages",              "summary": "List WAF packages" },
      { "method": "PATCH",  "path": "/zones/{zone_id}/firewall/waf/packages/{package_id}", "summary": "Update a WAF package" },
      { "method": "GET",    "path": "/zones/{zone_id}/firewall/waf/packages/{package_id}/rules", "summary": "List WAF rules" },
      { "method": "PATCH",  "path": "/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}", "summary": "Update a WAF rule" },
      { "method": "GET",    "path": "/zones/{zone_id}/rulesets",                           "summary": "List zone rulesets" },
      { "method": "POST",   "path": "/zones/{zone_id}/rulesets",                           "summary": "Create a zone ruleset" },
      { "method": "GET",    "path": "/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint", "summary": "Get a zone entry point ruleset" },
      { "method": "PUT",    "path": "/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint", "summary": "Update a zone entry point ruleset" },
      { "method": "POST",   "path": "/zones/{zone_id}/rulesets/{ruleset_id}/rules",        "summary": "Create a zone ruleset rule" },
      { "method": "PATCH",  "path": "/zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id}", "summary": "Update a zone ruleset rule" }
    ]
    

Toàn bộ đặc tả API của Cloudflare có hơn 2.500 điểm cuối. Mô hình đã thu hẹp phạm vi xuống còn các điểm cuối WAF và bộ quy tắc cần thiết mà không đưa bất kỳ phần nào của đặc tả vào cửa sổ ngữ cảnh. 

Mô hình cũng có thể xem chi tiết cấu trúc (schema) của một điểm cuối cụ thể trước khi thực hiện lệnh gọi đến điểm cuối đó. Tại đây, nó kiểm tra xem những giai đoạn nào có sẵn trong các bộ quy tắc vùng:
    
    
    async () => {
      const op = spec.paths['/zones/{zone_id}/rulesets']?.get;
      const items = op?.responses?.['200']?.content?.['application/json']?.schema;
      // Walk the schema to find the phase enum
      const props = items?.allOf?.[1]?.properties?.result?.items?.allOf?.[1]?.properties;
      return { phases: props?.phase?.enum };
    }
    
    {
      "phases": [
        "ddos_l4", "ddos_l7",
        "http_request_firewall_custom", "http_request_firewall_managed",
        "http_response_firewall_managed", "http_ratelimit",
        "http_request_redirect", "http_request_transform",
        "magic_transit", "magic_transit_managed"
      ]
    }
    

Hiện tại, tác nhân đã biết chính xác các giai đoạn cần thiết: `ddos_l7 `để bảo vệ chống lại các cuộc tấn công DDoS và `http_request_firewall_managed` cho WAF.

**Bước 2: Hành động trên API  
** Tác nhân chuyển sang sử dụng hàm `execute`. "Hộp cát"nhận được yêu cầu `cloudflare.request()` ứng dụng khách có thể thực hiện các cuộc gọi đã được xác thực đến API của Cloudflare. Đầu tiên, tác nhân kiểm tra xem những bộ quy tắc nào đã tồn tại trong khu vực đó:
    
    
    async () => {
      const response = await cloudflare.request({
        method: "GET",
        path: `/zones/${zoneId}/rulesets`
      });
      return response.result.map(rs => ({
        name: rs.name, phase: rs.phase, kind: rs.kind
      }));
    }
    
    [
      { "name": "DDoS L7",          "phase": "ddos_l7",                        "kind": "managed" },
      { "name": "Cloudflare Managed","phase": "http_request_firewall_managed", "kind": "managed" },
      { "name": "Custom rules",     "phase": "http_request_firewall_custom",   "kind": "zone" }
    ]
    

Tác nhân nhận thấy rằng các bộ quy tắc DDoS và WAF được quản lý đã tồn tại. Giờ đây, nó có thể xâu chuỗi các lệnh gọi để kiểm tra các quy tắc và cập nhật mức độ nhạy cảm trong một lần thực thi duy nhất:
    
    
    async () => {
      // Get the current DDoS L7 entrypoint ruleset
      const ddos = await cloudflare.request({
        method: "GET",
        path: `/zones/${zoneId}/rulesets/phases/ddos_l7/entrypoint`
      });
    
      // Get the WAF managed ruleset
      const waf = await cloudflare.request({
        method: "GET",
        path: `/zones/${zoneId}/rulesets/phases/http_request_firewall_managed/entrypoint`
      });
    }
    

Toàn bộ quá trình này, từ tìm kiếm đặc tả và kiểm tra chi tiết cấu trúc đến việc liệt kê các bộ quy tắc và lấy cấu hình DDoS và WAF, chỉ cần bốn lần gọi công cụ.

### Máy chủ MCP của Cloudflare

Chúng tôi bắt đầu với các máy chủ MCP dành cho từng sản phẩm riêng lẻ. Bạn muốn một tác nhân quản lý DNS? Hãy thêm [_máy chủ MCP cho DNS_](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/dns-analytics). Bạn muốn xem nhật ký Workers? Thêm [_máy chủ MCP Giám sát Workers_](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/). Mỗi máy chủ xuất ra một bộ công cụ cố định được ánh xạ tới các thao tác API. Cách này hiệu quả khi bộ công cụ còn nhỏ, nhưng API của Cloudflare có hơn 2.500 điểm cuối. Không một hệ thống máy chủ được bảo trì thủ công nào có thể đáp ứng được nhu cầu đó.

Máy chủ MCP của Cloudflare giúp đơn giản hóa việc này. Hai công cụ, khoảng 1.000 mã thông báo và bao phủ mọi điểm cuối trong API. Khi chúng ta thêm các sản phẩm mới, các đường dẫn mã `search()` và `execute()` vẫn sẽ được sử dụng để tìm và gọi chúng - không cần định nghĩa công cụ mới, không cần máy chủ MCP mới. Nó thậm chí còn hỗ trợ [_GraphQL Analytics API_](https://developers.cloudflare.com/analytics/graphql-api/) (API phân tích dữ liệu qua GraphQL).

Máy chủ MCP của chúng tôi được xây dựng dựa trên các thông số kỹ thuật MCP mới nhất. Nó tuân thủ chuẩn OAuth 2.1, sử dụng [_Workers OAuth Provider_](https://github.com/cloudflare/workers-oauth-provider) (dịch vụ cấp OAuth cho Workers của Cloudflare) để giới hạn phạm vi quyền của mã thông báo xuống mức đã được người dùng phê duyệt khi kết nối. Tác nhân chỉ có được những quyền hạn mà người dùng đã cấp phép một cách rõ ràng. 

Đối với các nhà phát triển, điều này có nghĩa là bạn có thể sử dụng một vòng lặp tác nhân đơn giản và vẫn cấp cho tác nhân của mình quyền truy cập vào toàn bộ API của Cloudflare với khả năng khám phá năng lực được tích hợp sẵn.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![images/BLOG-3184 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VC53BWNJ923RVB2YGTHM.png&w=715&h=738&f=webp&fit=cover&position=center)

### So sánh các phương pháp giảm thiểu ngữ cảnh

Đã có một số phương pháp được đưa ra để giảm số lượng mã thông báo mà các công cụ MCP tiêu thụ:

**Chế độ Mã phía máy khách** là thử nghiệm đầu tiên của chúng tôi. Mô hình này viết mã TypeScript dựa trên các SDK có kiểu dữ liệu và chạy nó trong một Dynamic Worker Loader (Cơ chế nạp Workers động) trên máy khách. Nhược điểm là nó đòi hỏi tác nhân phải được cung cấp kèm theo quyền truy cập "hộp cát" bảo mật. Chế độ Mã được triển khai trên [_Goose_](https://block.github.io/goose/blog/2025/12/15/code-mode-mcp/) và Claude SDK của Anthropic ở dạng [_Programmatic Tool Calling_](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) (Cơ chế gọi công cụ bằng mã lệnh).

**Giao diện dòng lệnh** là một hướng đi khác. Giao diện dòng lệnh (Command-line interfaces, CLI) có tính tự mô tả và bộc lộ các khả năng khi tác nhân khám phá. Các công cụ như [_OpenClaw_](https://openclaw.ai/) và [_Moltworker_](https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/) chuyển đổi máy chủ MCP thành CLI bằng cách sử dụng [_MCPorter_](https://github.com/steipete/mcporter) để cung cấp cho các tác nhân khả năng tiết lộ thông tin dần dần. Hạn chế rất rõ ràng: tác nhân cần một lớp vỏ bảo vệ, điều mà không phải môi trường nào cũng cung cấp và điều này tạo ra một bề mặt tấn công rộng hơn nhiều so với một môi trường biệt lập được cách ly.

Cơ chế **Tìm kiếm công cụ động** , như [_trong Claude Code của Anthropic_](https://x.com/trq212/status/2011523109871108570)giúp hiển thị một tập công cụ gọn hơn, có khả năng liên quan trực tiếp đến nhiệm vụ đang thực hiện. Nó thu hẹp phạm vi sử dụng ngữ cảnh nhưng lại yêu cầu một chức năng tìm kiếm cần được duy trì và đánh giá, và mỗi công cụ phù hợp vẫn sử dụng các mã thông báo.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![images/BLOG-3184 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47A6RDKCN3G22F2NEMK5FT.png&w=715&h=703&f=webp&fit=cover&position=center)

Mỗi phương pháp đều giải quyết một vấn đề thực tế. Nhưng đối với các máy chủ MCP nói riêng, Chế độ Mã phía máy chủ kết hợp các ưu điểm của chúng: chi phí mã thông báo cố định bất kể kích thước API, không cần sửa đổi ở phía tác nhân, khả năng khám phá dần dần được tích hợp sẵn và thực thi an toàn bên trong môi trường biệt lập. Tác nhân chỉ cần gọi hai công cụ bằng mã lệnh. Mọi thứ khác đều diễn ra trên máy chủ.

### Bắt đầu ngay hôm nay!

Máy chủ MCP của Cloudflare hiện khả dụng. Hãy trỏ trình khách MCP của bạn tới URL của máy chủ và bạn sẽ được chuyển hướng đến Cloudflare để ủy quyền và chọn các quyền cần cấp cho tác nhân của mình. Thêm cấu hình này vào trình khách MCP của bạn: 
    
    
    {
      "mcpServers": {
        "cloudflare-api": {
          "url": "https://mcp.cloudflare.com/mcp"
        }
      }
    }
    

Đối với quy trình CI/CD (tích hợp liên tục/triển khai liên tục), các tác vụ tự động hoá, hoặc nếu bạn muốn tự quản lý mã thông báo của mình, hãy tạo một mã thông báo API của Cloudflare với các quyền mà bạn cần. Cả mã thông báo người dùng và mã thông báo tài khoản đều được hỗ trợ và có thể được truyền dưới dạng mã thông báo dạng bearer trong tiêu đề `Authorization` (Ủy quyền).

Bạn có thể tìm thêm thông tin về các cấu hình thiết lập MCP khác nhau tại [_Kho lưu trữ MCP của Cloudflare_](https://github.com/cloudflare/mcp).

### Hướng về phía trước

Chế độ Mã giải quyết chi phí ngữ cảnh cho một API duy nhất. Nhưng các tác nhân hiếm khi chỉ liên hệ với một dịch vụ duy nhất. Một tác nhân của nhà phát triển có thể cần API của Cloudflare cùng với GitHub, cơ sở dữ liệu và máy chủ tài liệu nội bộ. Mỗi máy chủ MCP bổ sung đều mang lại áp lực lên cửa sổ ngữ cảnh tương tự như lúc ban đầu.

[_Cổng Máy chủ MCP của Cloudflare_](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) cho phép bạn thiết lập nhiều máy chủ MCP phía sau một cổng duy nhất với xác thực và kiểm soát truy cập thống nhất. Chúng tôi đang xây dựng một giải pháp tích hợp Chế độ Mã hàng đầu cho tất cả các máy chủ MCP của bạn, đồng thời cung cấp chúng cho tác nhân với cơ chế khám phá dần được tích hợp sẵn và cùng một mức tiêu thụ mã thông báo cố định, bất kể có bao nhiêu dịch vụ nằm phía sau cửa ngõ (gateway).

Trên trang này

Thảo luận trực tuyến

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fvi-vn%2Fcode-mode-mcp%2F&t=Ch%E1%BA%BF%20%C4%91%E1%BB%99%20M%C3%A3%3A%20cung%20c%E1%BA%A5p%20to%C3%A0n%20b%E1%BB%99%20APIcho%20t%C3%A1c%20nh%C3%A2n%20AItrong%20gi%E1%BB%9Bi%20h%E1%BA%A1n%201.000%20m%C3%A3%20th%C3%B4ng%20b%C3%A1o)[](https://x.com/intent/post?text=Ch%E1%BA%BF+%C4%91%E1%BB%99+M%C3%A3%3A+cung+c%E1%BA%A5p+to%C3%A0n+b%E1%BB%99+APIcho+t%C3%A1c+nh%C3%A2n+AItrong+gi%E1%BB%9Bi+h%E1%BA%A1n+1.000+m%C3%A3+th%C3%B4ng+b%C3%A1o&url=https%3A%2F%2Fblog.cloudflare.com%2Fvi-vn%2Fcode-mode-mcp%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fvi-vn%2Fcode-mode-mcp%2F)[](https://bsky.app/intent/compose?text=Ch%E1%BA%BF+%C4%91%E1%BB%99+M%C3%A3%3A+cung+c%E1%BA%A5p+to%C3%A0n+b%E1%BB%99+APIcho+t%C3%A1c+nh%C3%A2n+AItrong+gi%E1%BB%9Bi+h%E1%BA%A1n+1.000+m%C3%A3+th%C3%B4ng+b%C3%A1o+https%3A%2F%2Fblog.cloudflare.com%2Fvi-vn%2Fcode-mode-mcp%2F)[](https://mastodonshare.com/?text=Ch%E1%BA%BF+%C4%91%E1%BB%99+M%C3%A3%3A+cung+c%E1%BA%A5p+to%C3%A0n+b%E1%BB%99+APIcho+t%C3%A1c+nh%C3%A2n+AItrong+gi%E1%BB%9Bi+h%E1%BA%A1n+1.000+m%C3%A3+th%C3%B4ng+b%C3%A1o&url=https%3A%2F%2Fblog.cloudflare.com%2Fvi-vn%2Fcode-mode-mcp%2F)[](https://www.threads.net/intent/post?text=Ch%E1%BA%BF+%C4%91%E1%BB%99+M%C3%A3%3A+cung+c%E1%BA%A5p+to%C3%A0n+b%E1%BB%99+APIcho+t%C3%A1c+nh%C3%A2n+AItrong+gi%E1%BB%9Bi+h%E1%BA%A1n+1.000+m%C3%A3+th%C3%B4ng+b%C3%A1o+https%3A%2F%2Fblog.cloudflare.com%2Fvi-vn%2Fcode-mode-mcp%2F)

## Thẻ liên quan

[AI](https://blog.cloudflare.com/vi-vn/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/vi-vn/tag/workers/)[Nền tảng Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developer-platform/)[Nguồn mở](https://blog.cloudflare.com/vi-vn/tag/open-source/)[Nhà phát triển](https://blog.cloudflare.com/vi-vn/tag/developers/)[Tối ưu hóa](https://blog.cloudflare.com/vi-vn/tag/optimization/)[Workers AI](https://blog.cloudflare.com/vi-vn/tag/workers-ai/)

Theo dõi trên mạng xã hội

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Đăng ký để nhận thông báo bài viết mới

Địa chỉ email

Chúng tôi sẽ không bao giờ chia sẻ địa chỉ email của bạn.

Đăng ký

Cảm ơn bạn đã đăng ký! Hãy kiểm tra hộp thư đến để xác nhận.
