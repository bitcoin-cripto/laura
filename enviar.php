<?php
header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false]);
    exit;
}

$nombre  = htmlspecialchars(strip_tags(trim($_POST['nombre']  ?? '')));
$email   = htmlspecialchars(strip_tags(trim($_POST['email']   ?? '')));
$asunto  = htmlspecialchars(strip_tags(trim($_POST['asunto']  ?? 'Consulta general')));
$mensaje = htmlspecialchars(strip_tags(trim($_POST['mensaje'] ?? '')));

if (!$nombre || !$email || !filter_var($email, FILTER_VALIDATE_EMAIL) || !$mensaje) {
    http_response_code(400);
    echo json_encode(['ok' => false, 'error' => 'Datos incompletos o email inválido']);
    exit;
}

$destinatario = 'info@laurafernandeznodualidad.com';
$asunto_email = '=?UTF-8?B?' . base64_encode('Nuevo mensaje web: ' . $asunto) . '?=';

$cuerpo = '<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#f5f0e8;font-family:\'Inter\',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f5f0e8;padding:40px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;background:#fdfbf6;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(45,74,93,.12);">

        <!-- Cabecera -->
        <tr>
          <td style="background:#2d4a5d;padding:32px 40px;text-align:center;">
            <p style="margin:0;font-family:Georgia,serif;font-size:22px;color:#c9a96e;letter-spacing:.08em;">Laura Fernández</p>
            <p style="margin:6px 0 0;font-size:12px;color:rgba(253,251,246,.65);letter-spacing:.2em;text-transform:uppercase;">No Dualidad</p>
          </td>
        </tr>

        <!-- Cuerpo -->
        <tr>
          <td style="padding:40px 40px 32px;">
            <p style="margin:0 0 24px;font-size:13px;letter-spacing:.18em;text-transform:uppercase;color:#a8794f;font-weight:600;">Nuevo mensaje desde la web</p>
            <h1 style="margin:0 0 28px;font-size:22px;font-weight:700;color:#2d4a5d;line-height:1.3;">' . $asunto . '</h1>

            <!-- Datos del remitente -->
            <table width="100%" cellpadding="0" cellspacing="0" style="background:#f5f0e8;border-radius:10px;margin-bottom:28px;">
              <tr>
                <td style="padding:16px 20px;border-bottom:1px solid #efe6d6;">
                  <span style="font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#a8794f;font-weight:600;">Nombre</span><br>
                  <span style="font-size:15px;color:#3a3530;font-weight:500;">' . $nombre . '</span>
                </td>
              </tr>
              <tr>
                <td style="padding:16px 20px;">
                  <span style="font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#a8794f;font-weight:600;">Email de contacto</span><br>
                  <a href="mailto:' . $email . '" style="font-size:15px;color:#2d4a5d;font-weight:500;text-decoration:none;">' . $email . '</a>
                </td>
              </tr>
            </table>

            <!-- Mensaje -->
            <p style="margin:0 0 10px;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#a8794f;font-weight:600;">Mensaje</p>
            <div style="background:#f5f0e8;border-left:3px solid #c9a96e;border-radius:0 8px 8px 0;padding:18px 20px;font-size:15px;color:#3a3530;line-height:1.75;white-space:pre-wrap;">' . $mensaje . '</div>
          </td>
        </tr>

        <!-- Botón responder -->
        <tr>
          <td style="padding:0 40px 40px;text-align:center;">
            <a href="mailto:' . $email . '?subject=Re: ' . rawurlencode($asunto) . '"
               style="display:inline-block;background:#a8794f;color:#fff;font-size:14px;font-weight:600;
                      letter-spacing:.06em;padding:14px 36px;border-radius:40px;text-decoration:none;">
              Responder a ' . $nombre . '
            </a>
          </td>
        </tr>

        <!-- Pie -->
        <tr>
          <td style="background:#2d4a5d;padding:20px 40px;text-align:center;">
            <p style="margin:0;font-size:11px;color:rgba(253,251,246,.45);letter-spacing:.1em;">
              Mensaje enviado desde laurafernandeznodualidad.com
            </p>
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>';

$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: Web Laura <no-reply@laurafernandeznodualidad.com>\r\n";
$headers .= "Reply-To: {$nombre} <{$email}>\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

$ok = mail($destinatario, $asunto_email, $cuerpo, $headers);

echo json_encode(['ok' => $ok]);
