import folium
import webbrowser
import os
import tempfile
from folium.plugins import MarkerCluster
from branca.element import Figure


def show_map_with_route():
    map_tphcm = folium.Map(location=[10.776889, 106.700806], zoom_start=12, tiles='OpenStreetMap')
    # Adding tile layers
    folium.TileLayer('OpenStreetMap', attr="OpenStreetMap").add_to(map_tphcm)
    folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                     name='OpenTopoMap', 
                     attr="OpenTopoMap").add_to(map_tphcm)
    # Tạo danh sách rỗng cho các marker
    Post = []
    # Thêm layer và các bưu điện
    folium.LayerControl().add_to(map_tphcm)
    
    Post.append(folium.Marker(location=[10.780519673982457, 106.70014476621735], icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Thành phố Hồ Chí Minh</i>'),
              tooltip='Bưu điện Thành phố Hồ Chí Minh'))
    Post.append(folium.Marker(location=[10.780076834697786, 106.69987647398925],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Bến Thành</i>'),
              tooltip='Bưu điện Bến Thành'))
    Post.append(folium.Marker(location=[10.781273270580906, 106.69945020145809],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Sài Gòn</i>'),
              tooltip='Bưu điện Sài Gòn'))
    Post.append(folium.Marker(location=[10.780387955042666, 106.7006035512192],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Giao Dịch Quốc Tế Sài Gòn</i>'),
              tooltip='Bưu Điện Giao Dịch Quốc Tế Sài Gòn'))
    Post.append(folium.Marker(location=[10.781109908969258, 106.69991154129228],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Nguyễn Du</i>'),
              tooltip='Bưu Điện Nguyễn Du'))
    Post.append(folium.Marker(location=[10.79265500947989, 106.6952577341717],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Đa Kao</i>'),
              tooltip='Bưu Điện Đa Kao'))
    Post.append(folium.Marker(location=[10.788918207046553, 106.69126331712023],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Tân Định</i>'),
              tooltip='Bưu điện Tân Định'))
    Post.append(folium.Marker(location=[10.765066357556748, 106.69588716081546],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Trung Tâm Bưu Chính Sài Gòn</i>'),
              tooltip='Trung Tâm Bưu Chính Sài Gòn'))
    Post.append(folium.Marker(location=[10.759638024979667, 106.66740589952384],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Trung Tâm Bưu Chính Sài Gòn - Bưu Cục Chợ Lớn</i>'),
              tooltip='Trung Tâm Bưu Chính Sài Gòn - Bưu Cục Chợ Lớn'))
    

    Post.append(folium.Marker(location=[10.76386472122042, 106.66022608418389],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Trưng Nữ Vương</i>'),
              tooltip='Bưu Điện Trưng Nữ Vương'))
    Post.append(folium.Marker(location=[10.75572348776913, 106.6718022860288],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Nguyễn Duy Dương </i>'),
              tooltip='Bưu Điện Nguyễn Duy Dương'))
    Post.append(folium.Marker(location=[10.776068353178387, 106.6574598130189],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Cục Khai Thác Nội Tỉnh Hồ Chí Minh </i>'),
              tooltip='Bưu Cục Khai Thác Nội Tỉnh Hồ Chí Minh'))
    Post.append(folium.Marker(location=[10.767641799342156, 106.67375926884397],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Cục Quận 10</i>'),
              tooltip='Bưu Cục Quận 10'))
    Post.append(folium.Marker(location=[10.77625575486877, 106.65690992466898],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Cục Khai Thác Liên Tỉnh Hồ Chí Minh </i>'),
              tooltip='Bưu Cục Khai Thác Liên Tỉnh Hồ Chí Minh'))
    Post.append(folium.Marker(location=[10.759958562851024, 106.6572024148638],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Phó Cơ Điều </i>'),
              tooltip='Bưu Điện Phó Cơ Điều'))
    Post.append(folium.Marker(location=[10.765340480372355, 106.6641678148638],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Ngô Quyền</i>'),
              tooltip='Bưu Điện Ngô Quyền'))
    Post.append(folium.Marker(location=[10.766378999528833, 106.67031411117398],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Ấn Quang</i>'),
              tooltip='Bưu Điện Ấn Quang'))
    Post.append(folium.Marker(location=[10.765565780086428, 106.65380429952384],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Tôn Thất Hiệp</i>'),
              tooltip='Bưu Điện Tôn Thất Hiệp'))
    
    Post.append(folium.Marker(location=[10.749793816853172, 106.64221778602881],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Quận 6</i>'),
              tooltip='Bưu Điện Quận 6'))
    Post.append(folium.Marker(location=[10.74689289868615, 106.62791222144735],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Hậu Giang</i>'),
              tooltip='Bưu điện Hậu Giang'))
    Post.append(folium.Marker(location=[10.7381962472482, 106.73017471193016],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Phú Mỹ </i>'),
              tooltip='Bưu Điện Phú Mỹ'))
    Post.append(folium.Marker(location=[10.714246235100116, 106.73738448904152],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Quận 7 </i>'),
              tooltip='Bưu điện Quận 7'))
    Post.append(folium.Marker(location=[10.744990866301157, 106.65643545945515],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Quận 8</i>'),
              tooltip='Bưu Điện Quận 8'))
    Post.append(folium.Marker(location=[10.735208916055054, 106.656564205475],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Tạ Quang Bửu</i>'),
              tooltip='Bưu Điện Tạ Quang Bửu'))
    Post.append(folium.Marker(location=[10.791493752635482, 106.7306934957712],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>EMS VNpost</i>'),
              tooltip='EMS VNpost'))
    Post.append(folium.Marker(location=[10.818195872720759, 106.77249184735281],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Phước Bình </i>'),
              tooltip='Bưu điện Phước Bình'))
    Post.append(folium.Marker(location=[10.857046496434508, 106.75532116170616],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Thủ Đức </i>'),
              tooltip='Bưu điện Thủ Đức'))
    Post.append(folium.Marker(location=[10.8343324784891, 106.71334431660418],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Bình Triệu</i>'),
              tooltip='Bưu Điện Bình Triệu'))
    
    Post.append(folium.Marker(location=[10.704499920718812, 106.73719100765997],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện thị trấn Nhà Bè</i>'),
              tooltip='Bưu điện thị trấn Nhà Bè'))
    Post.append(folium.Marker(location=[10.713642476168138, 106.70038030150313],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Vietnam Post Lê Văn Lương</i>'),
              tooltip='Vietnam Post Lê Văn Lương'))
    Post.append(folium.Marker(location=[10.76029371165783, 106.61449104694232],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Bình Trị Đông</i>'),
              tooltip='Bưu điện Bình Trị Đông'))
    Post.append(folium.Marker(location=[10.805191097941576, 106.69447456286292],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Bình Thạnh</i>'),
              tooltip='Bưu điện Bình Thạnh'))
    Post.append(folium.Marker(location=[10.805191097941576, 106.71129737612279],
                  popup=folium.Popup('<i>Bưu điện Hàng Xanh</i>'), icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
              tooltip='Bưu điện Hàng Xanh'))
    Post.append(folium.Marker(location=[10.775399894402348, 106.69022036186234],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Quận 3</i>'),
              tooltip='Bưu điện Quận 3'))
    Post.append(folium.Marker(location=[10.822396764824115, 106.68850711395555],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Gò Vấp</i>'),
              tooltip='Bưu Điện Gò Vấp'))
    Post.append(folium.Marker(location=[10.841899284977384, 106.63823675755052],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Phan Huy Ích VNPOST </i>'),
              tooltip='Bưu Điện Phan Huy Ích VNPOST'))
    Post.append(folium.Marker(location=[10.797278416809684, 106.68093163972956],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Phú Nhuận</i>'),
              tooltip='Bưu điện Phú Nhuận'))
    Post.append(folium.Marker(location=[10.794510808293749, 106.66840544543382],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Lê Văn Sỹ</i>'),
              tooltip='Bưu Điện Lê Văn Sỹ'))
    
    Post.append(folium.Marker(location=[10.800628613728678, 106.65842011301109],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>VNPOST - Bưu Điện Tân Bình</i>'),
              tooltip='VNPOST - Bưu Điện Tân Bình'))
    Post.append(folium.Marker(location=[10.816056986212775, 106.6664881969214],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Tân Sơn Nhất</i>'),
              tooltip='Bưu Điện Tân Sơn Nhất'))
    Post.append(folium.Marker(location=[10.784815307399208, 106.62360785871186],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Tân Phú</i>'),
              tooltip='Bưu điện Tân Phú'))
    Post.append(folium.Marker(location=[10.780093650013157, 106.6341650323392],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Luỹ Bán Bích </i>'),
              tooltip='Bưu điện Luỹ Bán Bích'))
    Post.append(folium.Marker(location=[10.815110254303454, 106.57887382687062],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Vĩnh Lộc </i>'),
              tooltip='Bưu điện Vĩnh Lộc'))
    Post.append(folium.Marker(location=[10.81696165743005, 106.52026709619074],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Bình Chánh </i>'),
              tooltip='Bưu Điện Bình Chánh'))
    Post.append(folium.Marker(location=[10.41397825988566, 106.96176488037887],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Cần Giờ</i>'),
              tooltip='Bưu điện Cần Giờ'))
    Post.append(folium.Marker(location=[10.975123635953034, 106.49445183102168],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Củ Chi</i>'),
              tooltip='Bưu điện Củ Chi'))
    Post.append(folium.Marker(location=[10.89216706182972, 106.59595519233417],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu điện Hóc Môn</i>'),
              tooltip='Bưu điện Hóc Môn'))
    Post.append(folium.Marker(location=[10.85221357499071, 106.58702880162487],icon=folium.Icon(icon='glyphicon glyphicon-envelope', color='green'),
                  popup=folium.Popup('<i>Bưu Điện Phan Văn Hớn</i>'),
              tooltip='Bưu Điện Phan Văn Hớn'))
    
    # Thêm mã JavaScript
    script = """
    <script>
    function saveMarker(lat, lng) 
    {
    // Hiển thị marker vừa chọn trên console
    console.log('Đã chọn marker ở vị trí: ' + lat + ', ' + lng);

    // Thực hiện các hành động khác ở đây, ví dụ thay đổi màu sắc của marker
    let selectedMarker = L.marker([lat, lng]);
    selectedMarker.setIcon(new L.Icon({iconUrl: 'http://leafletjs.com/docs/images/leaf-red.png'}));
    selectedMarker.addTo(map_tphcm);
    }

    // Thêm popup với sự kiện "click" vào mỗi marker
    for (let marker of Post) 
    {
    marker.add_to(map_tphcm);
    marker.popup = folium.Popup('<a href="#" onclick="saveMarker(' + marker.location[0] + ', ' + marker.location[1] + '); return false;">Lưu Marker</a>');
    marker.on('click', function(e) {
        // Xác định vị trí của marker đã được chọn và hiển thị nó lên console
        let lat = e.latlng.lat;
        let lng = e.latlng.lng;
        console.log('Đã chọn marker ở vị trí: ' + lat + ', ' + lng);
    });
}

    </script>
    """


    map_tphcm.get_root().html.add_child(folium.Element(script))

    # Thêm popup với hàm JavaScript vào mỗi marker
    for marker in Post:
        marker.add_to(map_tphcm)
        marker.popup = folium.Popup('<a href="#" onclick="saveMarker(' + str(marker.location[0]) + ', ' + str(marker.location[1]) + '); return false;">Lưu Marker</a>')

    # Create a temporary HTML file and open it in the browser
    temp_file = tempfile.NamedTemporaryFile(suffix=".html", delete=False)
    map_tphcm.save(temp_file.name)
    webbrowser.open_new_tab(temp_file.name)
    return map_tphcm
    
    