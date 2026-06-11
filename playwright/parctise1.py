from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://axiom.qualcomm.com/")
    page.goto("https://axiom.qualcomm.com/#/home/dashboard")
    page.goto("https://login.microsoftonline.com/98e9ba89-e1a1-4e38-9007-8bdabc25de1d/oauth2/v2.0/authorize?client_id=eaa8ffd8-d85a-4b78-9199-66c72ab3e1d9&scope=user.read%20openid%20profile%20offline_access&redirect_uri=https%3A%2F%2Faxiom.qualcomm.com&client-request-id=019e67a0-c7b4-759f-8603-86bea37e5ef2&response_mode=fragment&client_info=1&nonce=019e67a0-c7b7-7b45-8008-4f3cb079be6f&state=eyJpZCI6IjAxOWU2N2EwLWM3YjYtN2NhMi1iNzYzLTkxYjMwYjZjMGVmYiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.24.1&response_type=code&code_challenge=S7evorIjuCdA8k1BkLWrW0ZziEoS21q99pgBIj-4x94&code_challenge_method=S256")
    page.goto("https://login.microsoftonline.com/98e9ba89-e1a1-4e38-9007-8bdabc25de1d/oauth2/v2.0/authorize?client_id=eaa8ffd8-d85a-4b78-9199-66c72ab3e1d9&scope=user.read%20openid%20profile%20offline_access&redirect_uri=https%3A%2F%2Faxiom.qualcomm.com&client-request-id=019e67a0-c7b4-759f-8603-86bea37e5ef2&response_mode=fragment&client_info=1&nonce=019e67a0-c7b7-7b45-8008-4f3cb079be6f&state=eyJpZCI6IjAxOWU2N2EwLWM3YjYtN2NhMi1iNzYzLTkxYjMwYjZjMGVmYiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.24.1&response_type=code&code_challenge=S7evorIjuCdA8k1BkLWrW0ZziEoS21q99pgBIj-4x94&code_challenge_method=S256&sso_reload=true")
    page.get_by_placeholder("Email, phone, or Skype").click()
    page.get_by_placeholder("Email, phone, or Skype").fill("tmanaval")
    page.get_by_placeholder("Email, phone, or Skype").press("Enter")
    page.get_by_placeholder("Email, phone, or Skype").fill("tmanaval@qti.qualcomm.com")
    page.get_by_placeholder("Email, phone, or Skype").press("Enter")
    page.locator("#i0118").press("CapsLock")
    page.get_by_placeholder("Password").fill("T")
    page.get_by_placeholder("Password").press("CapsLock")
    page.get_by_placeholder("Password").fill("Thamizh*123")
    page.get_by_placeholder("Password").press("Enter")
    page.goto("https://axiom.qualcomm.com/#code=1.ARMAibrpmKHhOE6QB4vavCXeHdj_qOpa2HhLkZlmxyqz4dkAAAATAA.BQABBAIAAAADAOz_BQD0_0V2b1N0c0FydGlmYWN0cwIAAAAAAE3NEKlGYJ4MOSeKiavvka3FRp9PdtloNbDTo9lZbOdOpyvSpevrSfx7Oh_b9fpQoOfzBCwHbVLW5cwjw2MfGFsaecgJAywTN25ywM-Xkmkr5Ht6vtJ4bTslW6kLPQUPHBswPTzbIprZnhnxCVn-c7JAwliFHFcHype3htN_aUdUbA6JcaM3wRedIrFxZAZxGWvULsu3ApKDOF_WMY9SO8RfA8ShZv44vmykfSJrhrD_kOQcYX9KwahVmqquJyJFzHi_muNSZMlPskAHLT8e57MvIC7VonQna1D6RyOVGvMEhJ0V9aqJ5ZSu2hQwPODxalXKnejH_lo-anBc_aONNhX0wgpAJmo7kxQNctf7v-5Sh6vS8Hm8oTHiVqbFz1YsSyDOTS_ZTx76AtrBHPU03aXHT6bMUPEq_vfWVSumFo1D2eA_w4UCzqUfLjOw35pcbELGRulmgZZV1FsvDHR7i4FcQc_i8JZsxrJKFK7vzZEdWL36u54S1EoRoAbSjxkd0S9jx_b0mjysh-utDaVaJlAXQGiLDw4Ns0LjQ8xOGiDwmNYT4mZa-Ij_ISZMSBDOFvWpnlragxgEf7ugN1bODvLGwUjPYPnPJmIpIEHlzhrSFNTICUYci70AJxQ9KWX-6FZ18Es5YmQQtmUOSzqcQZGp9UhaGncPSlA4rCS3Ew-vNhCq401H_I0ZuynjfTaKa1k0a7s0TKCNuo14D--nf_RSUafNkzDZ_jo703B8mOpUNBNcz340sHsAjQn49Wp_cxCQWkpUnDgWu8-DEcgJ8oSy4f3x3qNzSyI3kezvjEqcjzAxx7lU4-vGWXqXYTbnVSNqdYutg8_7aPG8jbHnW0RFLQbZCo8sqZRfEwyAYP9BU4dNcAw715lsf23vRWjDY0byi1WsVd74b6UVfM01kvnPrlrV6UsihEwh6GdhHoiZPj7coEjXs7LixiR-yY8feEu8H8PUHgPXf_5tA3p7sgac4wlWvjw6o1MSi0t2gVdcLQy9Z8m6NGXdcQ74isU8gQgEMJX_jVSMygqJ6qM8YkTIgrRs8WOEOml0RbWGxrBDb0chMe5-Do9tr40-YZmlmMHuxg0BUkovK6gF04km_MLpK9n1Rc-sB9v8Dnvq8WFpkSGYSRhBI8rV2WrB-8JLRAOFbWGCpHulPSp4EcKA9Kxni0D4kRhYiuRqmQR2xvRSSbb5zVypygjeNwYCc62-lLMxGtsJ0Z88XpvH_iAprPo8D2JuIb-rq2-hFgbLXzM2ZOizIMN2kryPw1qAVSczN4lFCAov_dvjc6GKIHN6-sulpjeU_yzpxIIL0hBKpwtI6KWfe2OpiPc7OSR_LnZO-Q3FtKvUY-3aDQDHkcKPBQymb2_angUnZPm_mMAlhv-D6K-OVR2y-Q4gAYf1gbqsb01LeFcrkUM_GnyegvdWUhwJBWmPFNNX54yPbYmDiXOg&client_info=eyJ1aWQiOiI5ZjBkNWZiZC1lMDZhLTQzMDEtOGE0OS05MTg0ODVmNjNjN2MiLCJ1dGlkIjoiOThlOWJhODktZTFhMS00ZTM4LTkwMDctOGJkYWJjMjVkZTFkIn0&state=eyJpZCI6IjAxOWU2N2EwLWM3YjYtN2NhMi1iNzYzLTkxYjMwYjZjMGVmYiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3d&session_state=005071da-1aae-c047-f94a-733f2d11e4c4")
    page.goto("https://axiom.qualcomm.com/#/home/dashboard")
    page.goto("https://axiom.qualcomm.com/#")
    page.goto("https://axiom.qualcomm.com/")
    page.goto("https://axiom.qualcomm.com/#/home/dashboard")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
